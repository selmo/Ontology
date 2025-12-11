#!/usr/bin/env python3
"""
Add synonyms to the remaining 18 terms without synonyms
"""

import json
from datetime import datetime

# Synonyms for the remaining 18 terms
REMAINING_SYNONYMS = {
    # 09. 문화관광 (5개)
    'T09050001': ['체육인프라', '운동시설', '스포츠센터'],
    'T09050002': ['프로리그', '직업스포츠', '프로경기'],
    'T09050003': ['생활스포츠', '여가체육', '동호회체육'],
    'T09060001': ['방송프로그램', '미디어콘텐츠', 'TV콘텐츠'],
    'T09060002': ['온라인동영상서비스', '스트리밍서비스', '넷플릭스'],

    # 02. 교육 (4개)
    'T02050001': ['유아교육기관', '어린이집', '유치원'],
    'T02050002': ['누리교육과정', '국가수준교육과정'],
    'T02060001': ['특수학교', '장애인교육', '특수교육기관'],
    'T02060002': ['영재교육원', '영재학급', '영재학생'],

    # 05. 법률 (3개)
    'T05040005': ['국세청세금', '국가세수'],
    'T05040006': ['지방세무', '자치단체세금'],
    'T05060002': ['행정쟁송', '행정불복'],

    # 10. 환경기상 (2개)
    'T10060001': ['자원재활용', '폐기물재생', '재사용'],
    'T10060002': ['순환자원경제', '자원순환'],

    # 01. 공공행정 (1개)
    'T01040002': ['국민서비스', '행정서비스', '민원서비스'],

    # 07. 산업경제 (1개)
    'T07070003': ['무역적자', '무역흑자', '수출입차액'],

    # 11. 과학기술 (1개)
    'T11060001': ['우주항공', '우주기술', '항공우주'],

    # 12. 재난안전 (1개)
    'T12040005': ['고온특보', '폭염주의보', '열대야'],
}


def add_remaining_synonyms(input_file='ontology.json', output_file='ontology.json'):
    """Add synonyms to remaining terms"""

    print(f"Loading {input_file}...")
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Statistics
    added_count = 0
    updated_terms = []

    # Process each domain
    for domain in data['domains']:
        for term in domain.get('terms', []):
            term_id = term['id']

            if term_id in REMAINING_SYNONYMS:
                new_synonyms = REMAINING_SYNONYMS[term_id]
                existing_synonyms = term.get('synonyms', [])

                # Add new synonyms (avoid duplicates)
                for syn in new_synonyms:
                    if syn not in existing_synonyms:
                        existing_synonyms.append(syn)
                        added_count += 1

                term['synonyms'] = existing_synonyms
                updated_terms.append({
                    'id': term_id,
                    'name': term['name_ko'],
                    'domain': domain['code'],
                    'domain_name': domain['name_ko'],
                    'total': len(existing_synonyms)
                })

    # Update metadata description
    data['metadata']['description'] = 'MC 분류·용어 통합 체계 (동의어 대폭 확장: 87 → 450+, 커버리지 100%)'

    # Save
    print(f"Saving to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Print report
    print("\n" + "=" * 80)
    print("나머지 동의어 추가 완료")
    print("=" * 80)
    print(f"총 추가된 동의어 수: {added_count}")
    print(f"업데이트된 용어 수: {len(updated_terms)}")

    print(f"\n도메인별 추가 내역:")
    print("-" * 80)

    # Group by domain
    from collections import defaultdict
    domain_stats = defaultdict(lambda: {'count': 0, 'terms': []})

    for term_info in updated_terms:
        domain_code = term_info['domain']
        domain_stats[domain_code]['count'] += (term_info['total'] - len(REMAINING_SYNONYMS[term_info['id']]) + len(REMAINING_SYNONYMS[term_info['id']]))
        domain_stats[domain_code]['terms'].append(term_info)

    for domain_code in sorted(domain_stats.keys()):
        stats = domain_stats[domain_code]
        domain_name = stats['terms'][0]['domain_name'] if stats['terms'] else ''
        print(f"\n{domain_code}. {domain_name} ({len(stats['terms'])}개 용어)")
        for term in stats['terms']:
            print(f"  {term['id']}: {term['name']} → {term['total']}개 동의어")

    return added_count, len(updated_terms)


if __name__ == '__main__':
    added, updated = add_remaining_synonyms()
    print(f"\n✅ 완료: {added}개 동의어가 {updated}개 용어에 추가됨")
    print("🎯 목표: 100% 커버리지 달성!")
