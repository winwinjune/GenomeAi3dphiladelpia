# -*- coding: utf-8 -*-
"""Chromosome-related condition references; contains no disease prediction model.

Run this file with %run in the existing chromosome notebook.
It exports a UTF-8 JSON resource and defines notebook/web helper functions.
"""

import copy
import html
import json
from pathlib import Path


DISEASE_REFERENCE_DB = {'schema_version': '1.1',
 'reviewed_on': '2026-10-24',
 'purpose': 'chromosome_related_condition_reference',
 'coverage_complete': False,
 'supported_chromosomes': ['chr1',
                           'chr2',
                           'chr3',
                           'chr4',
                           'chr5',
                           'chr6',
                           'chr7',
                           'chr8',
                           'chr9',
                           'chr10',
                           'chr11',
                           'chr12',
                           'chr13',
                           'chr14',
                           'chr15',
                           'chr16',
                           'chr17',
                           'chr18',
                           'chr19',
                           'chr20',
                           'chr21',
                           'chr22',
                           'chrX',
                           'chrY'],
 'disease_prediction_available': False,
 'display_title': '관련 질환 정보 · 영상 기반 질환 예측 아님',
 'conditions': [{'id': '1p36_deletion_syndrome',
                 'name_ko': '1p36 결실 증후군',
                 'name_en': '1p36 deletion syndrome',
                 'chromosomes': ['chr1'],
                 'region_reference': '1p36',
                 'mechanism_category': '결실',
                 'mechanism_summary': '1번 염색체 단완 1p36 구간의 결실과 관련되며, 말단·말단 인접 구간 결실 또는 복잡한 재배열이 포함될 수 '
                                      '있다.',
                 'evidence_needed': '1p36의 실제 결실 범위와 재배열 정보를 확인해야 한다.',
                 'image_limit': '현재 모델은 번호와 정상/이상 의심만 출력한다. 질환에 해당하는 결실 구간·범위는 확인되지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/1p36-deletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '1q211_microdeletion',
                 'name_ko': '1q21.1 미세결실',
                 'name_en': '1q21.1 microdeletion',
                 'chromosomes': ['chr1'],
                 'region_reference': '1q21.1',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '1번 염색체 1q21.1 구간의 일부 유전물질이 소실되는 변화이다. 증상과 발현 정도가 다양하며 뚜렷한 증상이 없는 '
                                      '경우도 있다.',
                 'evidence_needed': '재발성 결실 구간의 복제수 정보가 필요하며, 변화의 존재와 증상 여부를 동일하게 취급하면 안 된다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/1q211-microdeletion/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '2q37_deletion_syndrome',
                 'name_ko': '2q37 결실 증후군',
                 'name_en': '2q37 deletion syndrome',
                 'chromosomes': ['chr2'],
                 'region_reference': '2q37 / HDAC4 포함 구간',
                 'mechanism_category': '결실',
                 'mechanism_summary': '2번 염색체 장완 말단 부근 2q37의 결실과 관련된다. 결실 크기는 다양하고 HDAC4 소실이 여러 특징과 '
                                      '관련된다.',
                 'evidence_needed': '실제 결실 범위와 포함 유전자를 확인해야 한다.',
                 'image_limit': '현재 모델은 번호와 정상/이상 의심만 출력한다. 질환에 해당하는 결실 구간·범위는 확인되지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/2q37-deletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '3q29_microdeletion_syndrome',
                 'name_ko': '3q29 미세결실 증후군',
                 'name_en': '3q29 microdeletion syndrome',
                 'chromosomes': ['chr3'],
                 'region_reference': '3q29',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '3번 염색체 3q29 구간의 결실과 관련된다. 같은 결실이 있어도 임상 양상은 다양하며 관련 건강 문제가 뚜렷하지 '
                                      '않은 경우도 있다.',
                 'evidence_needed': '3q29 구간의 결실과 복제수 확인이 필요하다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/3q29-microdeletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'wolf_hirschhorn_syndrome',
                 'name_ko': '울프-허쉬호른 증후군',
                 'name_en': 'Wolf-Hirschhorn syndrome',
                 'chromosomes': ['chr4'],
                 'region_reference': '4p 말단 부근',
                 'mechanism_category': '결실',
                 'mechanism_summary': '4번 염색체 단완 말단 부근의 결실로 발생한다. 결실 크기와 소실 유전자에 따라 특징이 달라질 수 있다.',
                 'evidence_needed': '4p 결실의 구간·범위와 관련 유전자 정보를 확인해야 한다.',
                 'image_limit': '현재 모델은 번호와 정상/이상 의심만 출력한다. 질환에 해당하는 결실 구간·범위는 확인되지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/wolf-hirschhorn-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'cri_du_chat_syndrome',
                 'name_ko': '묘성증후군(고양이울음증후군)',
                 'name_en': 'Cri-du-chat syndrome',
                 'chromosomes': ['chr5'],
                 'region_reference': '5p 말단 결실',
                 'mechanism_summary': '5번 염색체 단완(p)의 말단 구간 결실로 발생한다. 결실 범위는 사례마다 다르다.',
                 'evidence_needed': '5p 말단의 결실 여부와 범위를 확인한 핵형 또는 분자유전학적 결과가 필요하다. 현재 모델은 결실 위치와 범위를 '
                                    '출력하지 않는다.',
                 'image_limit': '5번 염색체의 모든 이상이 이 질환을 의미하지 않는다. 번호만으로 질환을 판단할 수 없다.',
                 'visualization_policy': '실제 결실 구간이 확인된 경우에만 그 근거에 따라 구간을 표시한다. 교육용 결실 예시는 환자 분석과 분리한다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/cri-du-chat-syndrome/'}],
                 'mechanism_category': '결실',
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '6q24_related_transient_neonatal_diabetes_mellitus',
                 'name_ko': '6q24 관련 일과성 신생아 당뇨병',
                 'name_en': '6q24-related transient neonatal diabetes mellitus',
                 'chromosomes': ['chr6'],
                 'region_reference': '6q24 / PLAGL1 관련 구간',
                 'mechanism_category': '각인·발현/복제수',
                 'mechanism_summary': '6q24의 부계 발현 유전자 과발현과 관련된다. 부계 단친이염색체성, 부계 구간 중복, 모계 저메틸화 등 여러 '
                                      '원인이 있다.',
                 'evidence_needed': '복제수뿐 아니라 메틸화·각인과 부모 유래를 구분하는 정보가 필요하다.',
                 'image_limit': '염색체 모양만으로 메틸화·각인·부모 유래 및 유전자 발현 상태를 확인할 수 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/6q24-related-transient-neonatal-diabetes-mellitus/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '7q1123_duplication_syndrome',
                 'name_ko': '7q11.23 중복 증후군',
                 'name_en': '7q11.23 duplication syndrome',
                 'chromosomes': ['chr7'],
                 'region_reference': '7q11.23',
                 'mechanism_category': '미세중복',
                 'mechanism_summary': '7q11.23 구간의 추가 사본과 관련된다. 같은 구간의 결실로 발생하는 윌리엄스 증후군과는 구분해야 한다.',
                 'evidence_needed': '관련 구간이 결실인지 중복인지와 복제수를 구분해야 한다.',
                 'image_limit': '일반 핵형 사진에서 미세 중복을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 중복을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/7q1123-duplication-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'williams_syndrome',
                 'name_ko': '윌리엄스 증후군',
                 'name_en': 'Williams syndrome',
                 'chromosomes': ['chr7'],
                 'region_reference': '7q11.23',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '7번 염색체 특정 구간의 결실로 여러 인접 유전자가 소실되는 질환이다. ELN 등 여러 유전자의 소실이 특징과 '
                                      '관련된다.',
                 'evidence_needed': '7q11.23 구간의 결실 여부와 범위를 확인해야 한다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/williams-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'trichorhinophalangeal_syndrome_type_ii',
                 'name_ko': '모발-비-지골 증후군 2형(랑거-기디온 증후군)',
                 'name_en': 'Trichorhinophalangeal syndrome type II',
                 'chromosomes': ['chr8'],
                 'region_reference': '8q / TRPS1·EXT1·RAD21 포함 구간',
                 'mechanism_category': '결실',
                 'mechanism_summary': '8번 염색체 장완에서 TRPS1, EXT1, RAD21 등을 포함하는 인접 구간의 결실과 관련된다.',
                 'evidence_needed': '8q 결실 범위와 포함 유전자를 확인해야 하며 TRPS1 단독 변이로 생기는 1형과 구분해야 한다.',
                 'image_limit': '현재 모델은 번호와 정상/이상 의심만 출력한다. 질환에 해당하는 결실 구간·범위는 확인되지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/trichorhinophalangeal-syndrome-type-ii/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'kleefstra_syndrome',
                 'name_ko': '클리프스트라 증후군(EHMT1 관련)',
                 'name_en': 'Kleefstra syndrome',
                 'chromosomes': ['chr9'],
                 'region_reference': '9q34.3 / EHMT1',
                 'mechanism_category': '결실 또는 유전자 변이',
                 'mechanism_summary': '9q34.3에서 EHMT1을 포함한 결실 또는 EHMT1의 기능을 손상시키는 변이와 관련된다.',
                 'evidence_needed': '구간 결실과 EHMT1 유전자 변이를 구분할 수 있는 정보가 필요하다.',
                 'image_limit': '일부 원인은 유전자 수준의 변화이다. 번호나 형태 이상만으로 원인을 구별하거나 질환을 배제할 수 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/kleefstra-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '10q26_deletion_syndrome',
                 'name_ko': '10q26 결실 증후군',
                 'name_en': '10q26 deletion syndrome',
                 'chromosomes': ['chr10'],
                 'region_reference': '10q26',
                 'mechanism_category': '결실',
                 'mechanism_summary': '10번 염색체 장완 10q26 구간의 결실과 관련된다. 말단을 포함하거나 장완 내부의 더 작은 구간이 결실될 수 '
                                      '있다.',
                 'evidence_needed': '결실 위치와 범위를 확인해야 한다.',
                 'image_limit': '현재 모델은 번호와 정상/이상 의심만 출력한다. 질환에 해당하는 결실 구간·범위는 확인되지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/10q26-deletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'wagr_syndrome',
                 'name_ko': 'WAGR 증후군',
                 'name_en': 'WAGR syndrome',
                 'chromosomes': ['chr11'],
                 'region_reference': '11p13 / PAX6·WT1 포함 구간',
                 'mechanism_category': '결실',
                 'mechanism_summary': '11번 염색체 단완에서 PAX6와 WT1 등을 포함한 인접 유전자 구간의 결실과 관련된다.',
                 'evidence_needed': '결실 범위와 PAX6·WT1 포함 여부를 확인해야 한다.',
                 'image_limit': '현재 모델은 번호와 정상/이상 의심만 출력한다. 질환에 해당하는 결실 구간·범위는 확인되지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/wagr-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'pallister_killian_mosaic_syndrome',
                 'name_ko': '팔리스터-킬리안 모자이크 증후군',
                 'name_en': 'Pallister-Killian mosaic syndrome',
                 'chromosomes': ['chr12'],
                 'region_reference': 'i(12p) / 12p 사염색체성',
                 'mechanism_category': '등완염색체·모자이크',
                 'mechanism_summary': '주로 일부 세포에 추가 등완염색체 i(12p)가 있어 12번 단완 유전물질이 네 사본이 되는 변화와 관련된다.',
                 'evidence_needed': '추가 i(12p)의 존재와 세포별 구성, 모자이크 여부 등 사례 단위 정보가 필요하다.',
                 'image_limit': '단일 사진의 번호 분류만으로 추가 등완염색체와 조직·세포별 모자이크 구성을 평가할 수 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/pallister-killian-mosaic-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'trisomy_13',
                 'name_ko': '파타우 증후군(13번 삼염색체)',
                 'name_en': 'Trisomy 13',
                 'chromosomes': ['chr13'],
                 'region_reference': '13번 전체 또는 일부 유전물질',
                 'mechanism_category': '수적 이상',
                 'mechanism_summary': '흔한 형태는 13번 염색체가 세 사본인 경우이다. 전좌로 추가 유전물질이 생기거나 부분 삼염색체·모자이크 형태가 '
                                      '있을 수 있다.',
                 'evidence_needed': '전체 세포의 13번 사본 수와 구성, 필요시 복수 세포의 정보가 필요하다.',
                 'image_limit': '잘라낸 염색체 한 장으로 전체 사본 수를 셀 수 없다. 현재 모델은 전체 세포의 수적 이상을 분석하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/trisomy-13/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'ring_chromosome_14_syndrome',
                 'name_ko': '14번 고리염색체 증후군',
                 'name_en': 'Ring chromosome 14 syndrome',
                 'chromosomes': ['chr14'],
                 'region_reference': 'r(14)',
                 'mechanism_category': '고리염색체',
                 'mechanism_summary': '14번 염색체의 재배열로 고리 구조가 형성되는 변화와 관련된다. 형성 과정에서 말단 유전물질이 소실될 수 있다.',
                 'evidence_needed': '고리 구조의 존재, 기원 염색체, 소실 구간과 세포 구성을 확인해야 한다.',
                 'image_limit': '현재 모델은 고리 구조의 유형·기원·세포 구성을 직접 판정하지 않는다. 정상/이상 점수만으로 질환을 정할 수 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/ring-chromosome-14-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '15q11_q13_duplication_syndrome',
                 'name_ko': '15q11-q13 중복 증후군(모계 dup15q)',
                 'name_en': '15q11-q13 duplication syndrome',
                 'chromosomes': ['chr15'],
                 'region_reference': '15q11.2-q13.1',
                 'mechanism_category': '중복·각인',
                 'mechanism_summary': '모계 유래 15q11.2-q13.1 구간의 추가 사본과 관련된다. 장완 내부 중복 또는 등쌍동원체 15번 염색체 등 '
                                      '형태가 있다.',
                 'evidence_needed': '복제수·재배열 형태와 모계 유래 여부를 함께 확인해야 한다.',
                 'image_limit': '번호나 형태 이상만으로 복제수와 부모 유래를 확정할 수 없다. 현재 모델에는 각인 분석 기능이 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/15q11-q13-duplication-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '15q133_microdeletion',
                 'name_ko': '15q13.3 미세결실',
                 'name_en': '15q13.3 microdeletion',
                 'chromosomes': ['chr15'],
                 'region_reference': '15q13.3',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '15q13.3의 일부 구간 결실과 관련된다. 발현 정도가 다양하고 뚜렷한 증상이 없는 경우도 있다.',
                 'evidence_needed': '해당 구간의 실제 결실 범위와 임상 정보를 확인해야 한다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/15q133-microdeletion/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'angelman_syndrome',
                 'name_ko': '엔젤만 증후군',
                 'name_en': 'Angelman syndrome',
                 'chromosomes': ['chr15'],
                 'region_reference': 'UBE3A / 15q11.2-q13',
                 'mechanism_summary': '중추신경계에서 모계 유래 UBE3A의 기능 소실과 관련된다. 모계 구간 결실, UBE3A 변이, 부계 '
                                      '단친이염색체성, 각인 이상 등 여러 원인이 있다.',
                 'evidence_needed': 'UBE3A 및 관련 구간, 각인·부모 유래 등을 구분할 수 있는 분자유전학적 정보가 필요하다. 현재의 사진 분류에는 이 '
                                    '정보가 없다.',
                 'image_limit': '염색체 사진에서 확인하기 어려운 원인도 있다. 15번 이상이라는 결과만으로 프라더-윌리 증후군과 구별할 수 없다.',
                 'visualization_policy': '현재 결과에서 UBE3A 기능 소실이나 모계 구간 결실을 검출했다고 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/angelman-syndrome/'},
                             {'publisher': 'GeneReviews / NCBI Bookshelf',
                              'url': 'https://www.ncbi.nlm.nih.gov/books/NBK1144/'}],
                 'mechanism_category': '각인·유전자 기능',
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'prader_willi_syndrome',
                 'name_ko': '프라더-윌리 증후군',
                 'name_en': 'Prader-Willi syndrome',
                 'chromosomes': ['chr15'],
                 'region_reference': '15q11.2-q13',
                 'mechanism_summary': '15번 염색체의 특정 구간에서 부계 유래 유전자들의 기능 또는 발현이 소실되는 질환이다. 부계 구간 결실, 모계 '
                                      '단친이염색체성, 각인 이상 등 여러 원인이 있다.',
                 'evidence_needed': '해당 구간의 분자유전학적 정보와 각인·부모 유래를 구분하는 정보가 필요하다. 현재의 번호 및 정상/이상 분류 결과에는 '
                                    '이 정보가 없다.',
                 'image_limit': '15번 염색체라는 번호나 정상/이상 사진 점수만으로 이 질환을 선택하거나 배제할 수 없다.',
                 'visualization_policy': '현재 결과에서는 정상 참고 모형만 제공한다. 확인된 구간 정보 없이 15q 결실을 환자 모형에 표시하지 '
                                         '않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/prader-willi-syndrome/'},
                             {'publisher': 'GeneReviews / NCBI Bookshelf',
                              'url': 'https://www.ncbi.nlm.nih.gov/books/NBK1330/'}],
                 'mechanism_category': '각인·발현/복제수',
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '16p112_deletion_syndrome',
                 'name_ko': '16p11.2 결실 증후군',
                 'name_en': '16p11.2 deletion syndrome',
                 'chromosomes': ['chr16'],
                 'region_reference': '16p11.2',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '16번 염색체 단완 16p11.2 구간의 결실과 관련된다. 동일 구간의 중복과 구분해야 한다.',
                 'evidence_needed': '16p11.2의 결실 범위와 복제수를 확인해야 한다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/16p112-deletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '16p112_duplication',
                 'name_ko': '16p11.2 중복',
                 'name_en': '16p11.2 duplication',
                 'chromosomes': ['chr16'],
                 'region_reference': '16p11.2',
                 'mechanism_category': '미세중복',
                 'mechanism_summary': '16번 염색체 단완 16p11.2 구간의 추가 사본과 관련된다. 영향과 발현 정도는 사례마다 다르다.',
                 'evidence_needed': '해당 구간의 복제수와 실제 중복 범위를 확인해야 한다.',
                 'image_limit': '일반 핵형 사진에서 미세 중복을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 중복을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/16p112-duplication/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'smith_magenis_syndrome',
                 'name_ko': '스미스-마제니스 증후군',
                 'name_en': 'Smith-Magenis syndrome',
                 'chromosomes': ['chr17'],
                 'region_reference': '17p11.2 / RAI1',
                 'mechanism_category': '결실 또는 유전자 변이',
                 'mechanism_summary': '대부분 17p11.2에서 RAI1을 포함한 결실과 관련되며, RAI1 유전자 변이로 발생하는 경우도 있다.',
                 'evidence_needed': '17p11.2 결실과 RAI1 변이를 구분할 수 있는 정보가 필요하다.',
                 'image_limit': '일부 원인은 유전자 수준의 변화이다. 번호나 형태 이상만으로 원인을 구별하거나 질환을 배제할 수 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/smith-magenis-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'trisomy_18',
                 'name_ko': '에드워드 증후군(18번 삼염색체)',
                 'name_en': 'Trisomy 18',
                 'chromosomes': ['chr18'],
                 'region_reference': '18번 전체 또는 일부 유전물질',
                 'mechanism_category': '수적 이상',
                 'mechanism_summary': '흔한 형태는 18번 염색체가 세 사본인 경우이다. 일부 세포의 삼염색체 또는 추가 부분 유전물질과 관련된 형태도 '
                                      '있다.',
                 'evidence_needed': '전체 세포의 사본 수와 재배열 구성, 모자이크 여부를 확인해야 한다.',
                 'image_limit': '잘라낸 염색체 한 장으로 전체 사본 수를 셀 수 없다. 현재 모델은 전체 세포의 수적 이상을 분석하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/trisomy-18/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '19p1313_deletion_syndrome',
                 'name_ko': '19p13.13 결실 증후군',
                 'name_en': '19p13.13 deletion syndrome',
                 'chromosomes': ['chr19'],
                 'region_reference': '19p13.13',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '19번 염색체 단완 19p13.13 구간의 결실과 관련된다. 결실 크기와 포함 유전자는 사례마다 다를 수 있다.',
                 'evidence_needed': '실제 결실 범위와 포함 유전자를 확인해야 한다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/19p1313-deletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'ring_chromosome_20_syndrome',
                 'name_ko': '20번 고리염색체 증후군',
                 'name_en': 'Ring chromosome 20 syndrome',
                 'chromosomes': ['chr20'],
                 'region_reference': 'r(20)',
                 'mechanism_category': '고리염색체',
                 'mechanism_summary': '일부 또는 전체 세포에 고리 형태의 20번 염색체가 존재하는 변화와 관련된다. 모든 경우에 동일한 말단 결실이 있는 '
                                      '것은 아니다.',
                 'evidence_needed': '고리 구조와 기원 번호, 세포별 구성 및 모자이크 정보를 확인해야 한다.',
                 'image_limit': '현재 모델은 고리 구조의 유형·기원·세포 구성을 직접 판정하지 않는다. 정상/이상 점수만으로 질환을 정할 수 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/ring-chromosome-20-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'down_syndrome',
                 'name_ko': '다운증후군',
                 'name_en': 'Down syndrome',
                 'chromosomes': ['chr21'],
                 'region_reference': '21번 염색체 유전물질의 추가 사본',
                 'mechanism_summary': '흔한 형태는 21번 삼염색체이다. 전좌로 21번 유전물질이 추가되거나, 일부 세포에 추가 사본이 있는 모자이크 '
                                      '형태도 있다.',
                 'evidence_needed': '전체 세포의 염색체 구성·개수 또는 추가 21번 유전물질에 관한 정보가 필요하다. 모자이크 여부는 복수 세포의 정보가 '
                                    '필요하다.',
                 'image_limit': '잘라낸 21번 염색체 한 장의 정상/이상 결과로 삼염색체를 판단할 수 없다. 현재 모델은 전체 세포의 사본 수를 세지 않는다.',
                 'visualization_policy': '전체 세포의 수적 이상 정보가 없으면 세 번째 21번 염색체를 환자 결과처럼 추가하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/down-syndrome/'}],
                 'mechanism_category': '수적 이상',
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '22q112_deletion_syndrome',
                 'name_ko': '22q11.2 결실 증후군(디조지 증후군 등)',
                 'name_en': '22q11.2 deletion syndrome',
                 'chromosomes': ['chr22'],
                 'region_reference': '22q11.2',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '22번 염색체 22q11.2의 여러 인접 유전자를 포함한 구간 결실과 관련된다. 결실 범위와 임상 양상은 다양하다.',
                 'evidence_needed': '22q11.2 결실 여부와 실제 범위를 확인해야 한다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/22q112-deletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': '22q133_deletion_syndrome',
                 'name_ko': '22q13.3 결실 증후군(펠란-맥더미드 관련)',
                 'name_en': '22q13.3 deletion syndrome',
                 'chromosomes': ['chr22'],
                 'region_reference': '22q13.3 / SHANK3 포함 구간',
                 'mechanism_category': '결실',
                 'mechanism_summary': '22번 염색체 장완 말단 부근 결실과 관련되며 SHANK3 소실이 여러 특징과 관련된다. 고리염색체 22에 동반될 '
                                      '수도 있다.',
                 'evidence_needed': '22q13.3 결실 범위와 SHANK3 포함 여부, 재배열 형태를 확인해야 한다. SHANK3 변이 관련 질환의 모든 '
                                    '원인을 이 결실 설명이 포괄하지 않는다.',
                 'image_limit': '현재 모델은 번호와 정상/이상 의심만 출력한다. 질환에 해당하는 결실 구간·범위는 확인되지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/22q133-deletion-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'klinefelter_syndrome',
                 'name_ko': '클라인펠터 증후군',
                 'name_en': 'Klinefelter syndrome',
                 'chromosomes': ['chrX'],
                 'region_reference': '주로 47,XXY',
                 'mechanism_category': '수적 이상',
                 'mechanism_summary': '주로 X와 Y 외에 X가 한 사본 추가된 47,XXY 구성과 관련된다. 46,XY/47,XXY 모자이크 형태도 '
                                      '있다.',
                 'evidence_needed': '전체 성염색체 구성과 추가 X 여부, 모자이크 정보를 확인해야 한다.',
                 'image_limit': '잘라낸 염색체 한 장으로 전체 사본 수를 셀 수 없다. 현재 모델은 전체 세포의 수적 이상을 분석하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/klinefelter-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'turner_syndrome',
                 'name_ko': '터너 증후군',
                 'name_en': 'Turner syndrome',
                 'chromosomes': ['chrX'],
                 'region_reference': '45,X 또는 X 구조·모자이크 변화',
                 'mechanism_category': '수적·구조 이상',
                 'mechanism_summary': 'X 단염색체성 또는 두 번째 성염색체의 부분 소실·구조 변화와 관련된다. 일부 세포에만 변화가 있는 모자이크 형태도 '
                                      '있다.',
                 'evidence_needed': '전체 성염색체 구성과 X 구조, 복수 세포의 정보를 확인해야 한다.',
                 'image_limit': '단일 염색체 번호·정상/이상 결과로 전체 성염색체 구성이나 모자이크를 판단할 수 없다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/turner-syndrome/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'},
                {'id': 'y_chromosome_infertility',
                 'name_ko': 'Y 염색체 관련 불임(AZF 결실)',
                 'name_en': 'Y chromosome infertility',
                 'chromosomes': ['chrY'],
                 'region_reference': 'Y 염색체 AZF 구간',
                 'mechanism_category': '미세결실',
                 'mechanism_summary': '정자 생성과 관련된 Y 염색체 AZF 구간의 유전자 결실과 관련된다. 여러 유전자 또는 드물게 단일 유전자가 소실될 '
                                      '수 있다.',
                 'evidence_needed': 'AZF 구간의 유전적 결실 정보를 확인해야 한다. 일반 염색체 사진만으로 작은 결실을 평가하기 어렵다.',
                 'image_limit': '일반 핵형 사진에서 미세 결실을 확인하기 어려울 수 있다. 현재 모델은 해당 구간의 결실을 검출하거나 배제하지 않는다.',
                 'visualization_policy': '구간 표시는 출처 기반 교육용 예시로만 제공할 수 있다. 해당 사례에서 구간·유형이 확인되지 않으면 환자의 '
                                         '실제 이상 구조로 표시하지 않는다.',
                 'sources': [{'publisher': 'NIH/NLM MedlinePlus Genetics',
                              'url': 'https://medlineplus.gov/genetics/condition/y-chromosome-infertility/'}],
                 'reviewed_on': '2026-10-24',
                 'current_image_model_support': 'reference_lookup_only'}],
 'data_version': '2026-10-24-expanded',
 'chromosome_coverage_complete': True,
 'condition_count': 32,
 'coverage_note': '모든 염색체 번호에 최소 한 개의 관련 질환 설명이 있으나, 모든 유전질환을 포괄하지 않으며 영상 기반 질환 예측 성능을 뜻하지 않는다.'}


def _normalize_reference_chromosome(value):
    text = str(value).strip().upper().removeprefix("CHR").removesuffix("번").strip()
    allowed = {str(number) for number in range(1, 23)} | {"X", "Y"}
    if text not in allowed:
        raise ValueError("염색체 번호는 1~22, X, Y 중 하나여야 합니다.")
    return "chr" + text


def get_related_disease_info(chromosome):
    """Return an unranked reference list, independent of abnormality scores."""
    chromosome = _normalize_reference_chromosome(chromosome)
    conditions = [
        copy.deepcopy(condition)
        for condition in DISEASE_REFERENCE_DB["conditions"]
        if chromosome in condition["chromosomes"]
    ]
    return {
        "query_chromosome": chromosome,
        "display_mode": "reference_only",
        "coverage_complete": False,
        "disease_prediction_available": False,
        "reference_status": "registered" if conditions else "no_reference_registered",
        "related_conditions": conditions,
        "message": (
            "염색체 번호로 조회한 관련 질환 예시입니다. 질환 순위·발병 확률·영상 기반 질환 판정이 아닙니다."
            if conditions else
            "현재 DB에 등록된 설명이 없습니다. 관련 질환이 없다는 뜻은 아닙니다."
        ),
    }


def build_related_disease_response(prediction_result):
    """Web-ready response using only the top chromosome candidate for lookup."""
    candidates = prediction_result.get("number_candidates")
    if not candidates or "번호 후보" not in candidates[0]:
        raise ValueError("predict_chromosome 결과의 번호 후보가 필요합니다.")
    response = get_related_disease_info(candidates[0]["번호 후보"])
    response["chromosome_is_confirmed"] = False
    response["selection_basis"] = "unconfirmed_top_chromosome_candidate"
    response["notice"] = "번호 후보가 달라지면 조회되는 관련 질환 정보도 달라집니다."
    return response


def related_disease_html(response):
    """Render source-linked reference cards; never display disease probabilities."""
    esc = lambda value: html.escape(str(value), quote=True)
    cards = []
    for condition in response["related_conditions"]:
        sources = " · ".join(
            '<a href="{}" target="_blank" rel="noopener noreferrer">{}</a>'.format(
                esc(source["url"]), esc(source["publisher"])
            ) for source in condition["sources"]
        )
        fields = [
            ("관련 구간·유형", condition["region_reference"] + " / " + condition["mechanism_category"]),
            ("관련 유전적 변화", condition["mechanism_summary"]),
            ("판별에 필요한 추가 근거", condition["evidence_needed"]),
            ("현재 영상 분석의 한계", condition["image_limit"]),
        ]
        body = "".join(
            '<p style="margin:8px 0"><b>{}</b><br>{}</p>'.format(esc(label), esc(value))
            for label, value in fields
        )
        cards.append(
            '<article style="border:1px solid #d9e2ec;border-radius:12px;padding:18px;margin:12px 0">'
            '<h3 style="margin:0 0 10px">{}</h3>{}<p>출처: {}</p></article>'.format(
                esc(condition["name_ko"]), body, sources
            )
        )
    return (
        '<section style="font-family:Malgun Gothic,sans-serif;line-height:1.65;max-width:950px">'
        '<h2>관련 질환 정보 · {}</h2>'
        '<p style="background:#eef4fb;padding:12px;border-radius:8px">{}</p>'
        '<p>조회 기준은 AI의 미확인 번호 후보입니다. 등록 목록은 전체 관련 질환을 포괄하지 않습니다.</p>'
        '{}</section>'
    ).format(esc(response["query_chromosome"]), esc(response["message"]), "".join(cards))


def show_related_diseases(prediction_result):
    from IPython.display import HTML, display
    response = build_related_disease_response(prediction_result)
    display(HTML(related_disease_html(response)))
    return response


def export_disease_reference(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    output_path = directory / "chromosome_related_diseases_v1.json"
    output_path.write_text(
        json.dumps(DISEASE_REFERENCE_DB, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


if __name__ == "__main__":
    destination = Path(r"C:\chromosome_ai\resources") if __import__("os").name == "nt" else Path(__file__).resolve().parent
    output_path = export_disease_reference(destination)
    print("관련 질환 DB 준비 완료:", len(DISEASE_REFERENCE_DB["supported_chromosomes"]), "개 염색체, 질환·염색체 변화 설명", len(DISEASE_REFERENCE_DB["conditions"]), "개")
    print("JSON 저장 위치:", output_path)
    print("현재 노트북의 다음 셀에서 실행: related_result = show_related_diseases(demo_result)")
