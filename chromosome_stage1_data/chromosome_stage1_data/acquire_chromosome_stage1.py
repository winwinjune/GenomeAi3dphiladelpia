"""Download public chromosome samples; preserve raw labels, do not train or split."""
import concurrent.futures as cf
import urllib.request, urllib.parse, json, hashlib, zipfile, tarfile, io, csv, collections
from pathlib import Path, PurePosixPath
from datetime import datetime, timezone
from PIL import Image
import numpy as np

BASE = Path(__file__).resolve().parent
WORK = BASE / 'chromosome_acquisition_2026-10-21'
PACK = WORK / 'chromosome_stage1_data'
DOWNLOADS = WORK / 'downloads'
PACK.mkdir(parents=True, exist_ok=True)
DOWNLOADS.mkdir(exist_ok=True)
SOURCES = [
    ('CHROMA', 'Changchun-Yang/CHROMA', 'f96033f634a6058f319c03f4f6e3ff8f5f74a768'),
    ('BR-ChromNet', 'frankchen121212/BR-ChromNet', '6dfa8e7d745dc19b6f7c19373ac0f2e8a3133cdd'),
    ('CIR-Net', 'CloudDataLab/CIR-Net', 'bef2d815116cb3612f70da4d9a7893919e439f09'),
]
NOW = datetime.now(timezone.utc).isoformat()

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'ChromosomeDatasetAcquisition/1.0'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read()
        except Exception:
            if attempt == 2: raise

def acquire(source):
    name, repo, branch = source
    meta = json.loads(fetch(f'https://api.github.com/repos/{repo}/commits/{branch}'))
    sha = meta['sha']
    url = f'https://codeload.github.com/{repo}/zip/{sha}'
    b = fetch(url)
    archive = DOWNLOADS / (name + '.zip')
    archive.write_bytes(b)
    out = PACK / name
    out.mkdir(exist_ok=True)
    extracted = 0
    with zipfile.ZipFile(io.BytesIO(b)) as z:
        bad = z.testzip()
        if bad: raise ValueError(f'{name}: broken ZIP member {bad}')
        for member in z.infolist():
            parts = PurePosixPath(member.filename).parts
            rel = PurePosixPath(*parts[1:])
            if member.is_dir() or '..' in rel.parts: continue
            s = str(rel)
            keep = s in ('README.md', 'LICENSE')
            keep |= name == 'CHROMA' and s.startswith('open_data/') and s.endswith('.png')
            keep |= name == 'BR-ChromNet' and s.startswith('data/') and s.endswith(('.png', '.npy'))
            keep |= name == 'CIR-Net' and s == 'data/origin.tar.gz'
            if keep:
                target = out / s
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(z.read(member))
                extracted += 1
    if name == 'CIR-Net':
        tarpath = out / 'data/origin.tar.gz'
        with tarfile.open(tarpath, 'r:gz') as t:
            for m in t.getmembers():
                if not m.isfile(): continue
                rel = PurePosixPath(m.name)
                if rel.is_absolute() or '..' in rel.parts: raise ValueError('Unsafe archive member')
                target = out / 'data' / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(t.extractfile(m).read())
        tarpath.unlink()  # raw pixels retained, avoid duplicate packed copy
    result = dict(name=name, repository=f'https://github.com/{repo}', branch=branch,
                  commit=sha, archive_url=url, retrieved_at_utc=NOW,
                  archive_sha256=hashlib.sha256(b).hexdigest(), archive_bytes=len(b))
    print('DOWNLOADED', name, len(b), 'bytes', 'commit', sha, flush=True)
    return result

with cf.ThreadPoolExecutor(max_workers=3) as pool:
    source_results = list(pool.map(acquire, SOURCES))

rows, masks, errors = [], [], []
for name, repo, branch in SOURCES:
    for p in sorted((PACK / name).rglob('*')):
        if p.suffix.lower() not in ('.png', '.tif', '.tiff', '.npy'): continue
        rel = p.relative_to(PACK).as_posix()
        try:
            if p.suffix == '.npy':
                a = np.load(p, allow_pickle=False)
                img = p.with_suffix('.png')
                with Image.open(img) as im:
                    if tuple(a.shape[:2]) != (im.height, im.width):
                        raise ValueError(f'mask/image size mismatch: {a.shape} vs {im.size}')
                vals = np.unique(a).tolist()
                masks.append(dict(path=rel, shape=list(a.shape), dtype=str(a.dtype), values=vals,
                                  image=img.relative_to(PACK).as_posix()))
                continue
            with Image.open(p) as im:
                im.verify()
            with Image.open(p) as im:
                im.load(); width, height, mode = im.width, im.height, im.mode
                pixels_sha = hashlib.sha256(im.convert('L').tobytes() + f'{width}x{height}'.encode()).hexdigest()
            parts = p.relative_to(PACK / name).parts
            task = label = chr_label = ''
            mask = ''
            if name == 'CHROMA':
                if parts[1] == 'sta_ab':
                    task='structural_normal_abnormal'; label=parts[-2]
                    chr_label=parts[2].replace('sta_dist_', '').removesuffix('_2')
                elif parts[1] == 'unsta_ab': task='unstable_morphology'; label=parts[-2]
                else: task='chromosome_identity'; label=parts[-2]; chr_label=label
            elif name == 'BR-ChromNet':
                task='variant_region_mask'; label=parts[-2]; chr_label=parts[1]
                mask=p.with_suffix('.npy').relative_to(PACK).as_posix()
            else:
                task='chromosome_identity'; label=p.name.split('.')[-2]; chr_label='source_class_' + label
            b = p.read_bytes()
            rows.append(dict(path=rel, dataset=name, task=task, label=label,
                             chromosome_or_variant=chr_label, width=width, height=height, mode=mode,
                             mask_path=mask, patient_id='', patient_group_verified='no',
                             disease_label='', disease_label_verified='no', bytes=len(b),
                             sha256=hashlib.sha256(b).hexdigest(), grayscale_pixels_sha256=pixels_sha))
        except Exception as e:
            errors.append(dict(path=rel, error=str(e)))

checks=collections.Counter((r['dataset'],r['task'],r['label']) for r in rows)
counts={name:sum(r['dataset']==name for r in rows) for name,_,_ in SOURCES}
if errors: raise RuntimeError(json.dumps(errors, ensure_ascii=False))
expected={'CHROMA':1004, 'BR-ChromNet':30, 'CIR-Net':2986}
if counts != expected: raise ValueError(f'Published subset changed: {counts} != {expected}')
if len(masks)!=30: raise ValueError('Expected 30 BR masks')

groups=collections.defaultdict(list)
for r in rows: groups[r['grayscale_pixels_sha256']].append(r['path'])
duplicates=[v for v in groups.values() if len(v)>1]
with (PACK/'manifest.csv').open('w',newline='',encoding='utf-8-sig') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
(PACK/'sources.json').write_text(json.dumps(source_results,ensure_ascii=False,indent=2),encoding='utf-8')
quality=dict(image_files=len(rows),mask_files=len(masks),decoded_images=len(rows),
             corrupt_images=errors,counts=counts,mask_validation=masks,
             label_counts=[dict(dataset=k[0],task=k[1],label=k[2],count=v) for k,v in sorted(checks.items())],
             duplicate_pixel_groups=duplicates,
             note='No patient identities inferred. No train/validation/test split created. Labels preserved from original sources.')
(PACK/'quality_report.json').write_text(json.dumps(quality,ensure_ascii=False,indent=2),encoding='utf-8')
(WORK/'status.json').write_text(json.dumps(dict(counts=counts,masks=len(masks),duplicates=len(duplicates)),indent=2))
print('VERIFIED', counts, 'masks',len(masks),'duplicate groups',len(duplicates),flush=True)
