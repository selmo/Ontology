#!/usr/bin/env python3
"""
Analyze synonym distribution in ontology.json
"""

import json
from collections import defaultdict

def analyze_synonyms(filepath='ontology.json'):
    """Analyze current synonym coverage"""

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Statistics
    total_terms = 0
    terms_with_synonyms = 0
    total_synonyms = 0
    domain_stats = defaultdict(lambda: {
        'total_terms': 0,
        'terms_with_synonyms': 0,
        'total_synonyms': 0,
        'terms_without_synonyms': []
    })

    # Analyze each domain
    for domain in data['domains']:
        domain_code = domain['code']
        domain_name = domain['name_ko']

        # Process terms at domain level
        for term in domain.get('terms', []):
            total_terms += 1
            domain_stats[domain_code]['total_terms'] += 1

            synonyms = term.get('synonyms', [])
            if synonyms:
                terms_with_synonyms += 1
                domain_stats[domain_code]['terms_with_synonyms'] += 1
                total_synonyms += len(synonyms)
                domain_stats[domain_code]['total_synonyms'] += len(synonyms)
            else:
                # Term without synonyms
                domain_stats[domain_code]['terms_without_synonyms'].append({
                    'id': term['id'],
                    'name': term['name_ko'],
                    'name_en': term.get('name_en', ''),
                    'acronym': term.get('acronym', '')
                })

    # Print report
    print("=" * 80)
    print("동의어 분석 보고서")
    print("=" * 80)
    print(f"\n전체 통계:")
    print(f"  - 총 용어 수: {total_terms}")
    print(f"  - 동의어 보유 용어: {terms_with_synonyms} ({terms_with_synonyms/total_terms*100:.1f}%)")
    print(f"  - 동의어 미보유 용어: {total_terms - terms_with_synonyms} ({(total_terms-terms_with_synonyms)/total_terms*100:.1f}%)")
    print(f"  - 총 동의어 수: {total_synonyms}")
    print(f"  - 평균 동의어/용어: {total_synonyms/total_terms:.2f}")
    print(f"  - 목표: 250+ 동의어 (현재 {total_synonyms}, 부족 {max(0, 250-total_synonyms)})")

    print(f"\n도메인별 통계:")
    print("-" * 80)

    for domain in data['domains']:
        domain_code = domain['code']
        domain_name = domain['name_ko']
        stats = domain_stats[domain_code]

        if stats['total_terms'] == 0:
            continue

        coverage = stats['terms_with_synonyms'] / stats['total_terms'] * 100 if stats['total_terms'] > 0 else 0
        avg_syn = stats['total_synonyms'] / stats['total_terms'] if stats['total_terms'] > 0 else 0

        print(f"{domain_code}. {domain_name}")
        print(f"  - 용어: {stats['total_terms']}")
        print(f"  - 동의어 보유: {stats['terms_with_synonyms']} ({coverage:.1f}%)")
        print(f"  - 총 동의어: {stats['total_synonyms']}")
        print(f"  - 평균: {avg_syn:.2f}")
        print(f"  - 동의어 미보유 용어 수: {len(stats['terms_without_synonyms'])}")

    # Print terms without synonyms by domain
    print("\n" + "=" * 80)
    print("동의어 미보유 용어 목록 (우선순위 순)")
    print("=" * 80)

    # Sort domains by number of terms without synonyms
    sorted_domains = sorted(
        [(code, stats) for code, stats in domain_stats.items()],
        key=lambda x: len(x[1]['terms_without_synonyms']),
        reverse=True
    )

    for domain_code, stats in sorted_domains:
        if not stats['terms_without_synonyms']:
            continue

        # Find domain name
        domain_name = next(d['name_ko'] for d in data['domains'] if d['code'] == domain_code)

        print(f"\n{domain_code}. {domain_name} ({len(stats['terms_without_synonyms'])}개)")
        print("-" * 80)

        for term in stats['terms_without_synonyms'][:10]:  # Show first 10
            acronym_str = f" [{term['acronym']}]" if term['acronym'] else ""
            en_str = f" | {term['name_en']}" if term['name_en'] else ""
            print(f"  {term['id']}: {term['name']}{acronym_str}{en_str}")

        if len(stats['terms_without_synonyms']) > 10:
            print(f"  ... 외 {len(stats['terms_without_synonyms']) - 10}개")

    print("\n" + "=" * 80)
    print("권장 작업:")
    print("=" * 80)
    print(f"1. 동의어 추가 목표: 최소 {max(0, 250-total_synonyms)}개 추가")
    print(f"2. 우선순위 도메인: {', '.join([next(d['name_ko'] for d in data['domains'] if d['code'] == code) for code, _ in sorted_domains[:3]])}")
    print(f"3. 목표 커버리지: 현재 {terms_with_synonyms/total_terms*100:.1f}% → 80%+")

if __name__ == '__main__':
    analyze_synonyms()
