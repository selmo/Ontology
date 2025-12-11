#!/usr/bin/env python3
"""
Update ontology.json:
1. Remove RELATED_TO relationships from terms
2. Add SIMILAR_TO relationships between classifications
"""

import json
from datetime import datetime

# Define similar classifications (cross-domain similar concepts)
SIMILAR_CLASSIFICATIONS = [
    # 교육-과학기술 연계
    ('C02040001', 'C11010001'),  # 고등교육 ↔ 연구개발
    ('C02040003', 'C11050001'),  # 산학협력 ↔ 기술혁신·특허

    # 보건의료-사회복지 연계
    ('C03030001', 'C04020001'),  # 보건의료인력 ↔ 복지시설
    ('C03040001', 'C04010001'),  # 건강보험 ↔ 사회보장
    ('C03050001', 'C04040001'),  # 질병관리 ↔ 고령사회

    # 재정금융-공공행정 연계
    ('C06010001', 'C01040001'),  # 국가예산 ↔ 국가정책·사업
    ('C06030001', 'C01020001'),  # 지방재정 ↔ 지방행정·자치

    # 산업경제-디지털커머스 연계
    ('C07010001', 'C08010001'),  # 이커머스·유통 ↔ 이커머스 플랫폼
    ('C07030001', 'C08020001'),  # 고용·노동 ↔ 온라인 유통
    ('C07040001', 'C08030001'),  # 창업·벤처 ↔ 디지털 결제

    # 재난안전-환경기상 연계
    ('C12040001', 'C10030001'),  # 자연재난 ↔ 기상·기후
    ('C12040004', 'C10030001'),  # 지진 ↔ 기상·기후
    ('C12040002', 'C10030001'),  # 태풍 ↔ 기상·기후

    # 문화관광-교육 연계
    ('C09010001', 'C02030001'),  # 문화유산 ↔ 학교교육
    ('C09030001', 'C02020001'),  # 문화시설 ↔ 평생교육

    # 법률-공공행정 연계
    ('C05010001', 'C01040001'),  # 법령·법규 ↔ 국가정책·사업
    ('C05030001', 'C01040003'),  # 법률서비스 ↔ 대민서비스

    # 과학기술-산업경제 연계
    ('C11040001', 'C07020001'),  # ICT·정보기술 ↔ 산업통계
    ('C11050001', 'C07040001'),  # 기술혁신·특허 ↔ 창업·벤처

    # 환경기상-과학기술 연계
    ('C10020001', 'C11010001'),  # 기후변화 ↔ 연구개발
    ('C10050001', 'C11030001'),  # 신재생에너지 ↔ 공학기술
]


def update_ontology(input_file='ontology.json', output_file='ontology.json'):
    """Update ontology.json"""

    print(f"Loading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Step 1: Remove RELATED_TO from all terms
    print("\n1. RELATED_TO 제거 중...")
    removed_count = 0

    for domain in data['domains']:
        for term in domain.get('terms', []):
            if 'related_terms' in term:
                removed_count += len(term['related_terms'])
                del term['related_terms']

    print(f"   ✓ {removed_count}개 RELATED_TO 관계 제거됨")

    # Step 2: Add SIMILAR_TO to classifications
    print("\n2. SIMILAR_TO 추가 중...")

    # Build classification lookup
    clsf_map = {}

    def index_classifications(classifications, domain_code):
        for clsf in classifications:
            clsf_map[clsf['id']] = {
                'ref': clsf,
                'domain': domain_code
            }
            if 'children' in clsf:
                index_classifications(clsf['children'], domain_code)

    for domain in data['domains']:
        index_classifications(domain.get('classifications', []), domain['code'])

    # Add similar_to relationships
    added_count = 0

    for clsf_id1, clsf_id2 in SIMILAR_CLASSIFICATIONS:
        if clsf_id1 in clsf_map and clsf_id2 in clsf_map:
            clsf1 = clsf_map[clsf_id1]['ref']
            clsf2 = clsf_map[clsf_id2]['ref']

            # Add to clsf1
            if 'similar_to' not in clsf1:
                clsf1['similar_to'] = []
            if clsf_id2 not in clsf1['similar_to']:
                clsf1['similar_to'].append(clsf_id2)
                added_count += 1

            # Add to clsf2 (bidirectional)
            if 'similar_to' not in clsf2:
                clsf2['similar_to'] = []
            if clsf_id1 not in clsf2['similar_to']:
                clsf2['similar_to'].append(clsf_id1)
                added_count += 1

    print(f"   ✓ {added_count}개 SIMILAR_TO 관계 추가됨 ({len(SIMILAR_CLASSIFICATIONS)}개 쌍)")

    # Step 3: Update metadata
    data['metadata']['version'] = '3.10.0'
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    data['metadata']['description'] = 'MC 분류·용어 통합 체계 (관계 재구조화: SIMILAR_TO 추가, RELATED_TO 제거)'

    # Save
    print(f"\nSaving to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Print summary
    print("\n" + "=" * 80)
    print("관계 재구조화 완료")
    print("=" * 80)
    print(f"\n변경사항:")
    print(f"  ✗ RELATED_TO (Term → Term): {removed_count}개 제거")
    print(f"  ✓ SIMILAR_TO (Classification → Classification): {added_count}개 추가")

    print(f"\n새로운 관계 구조:")
    print(f"  1. PARENT_OF: Classification → Classification (계층)")
    print(f"  2. PARENT_OF: Term → Term (계층)")
    print(f"  3. BELONGS_TO: Term → Classification (소속)")
    print(f"  4. SYNONYM_OF: Term → Synonym (동의어)")
    print(f"  5. SIMILAR_TO: Classification → Classification (유사) ← NEW")

    return removed_count, added_count


if __name__ == '__main__':
    removed, added = update_ontology()
    print(f"\n✅ 완료: {removed}개 제거, {added}개 추가")
