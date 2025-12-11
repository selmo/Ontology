#!/usr/bin/env python3
"""
Analyze standard reference coverage by domain
"""

import json

def analyze_coverage(filepath='ontology.json'):
    """Analyze standard reference coverage"""

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    clsf_with_refs = 0
    clsf_total = 0
    term_with_refs = 0
    term_total = 0

    domain_stats = {}

    for domain in data['domains']:
        domain_code = domain['code']
        domain_name = domain['name_ko']

        # Count classifications
        def count_clsf(classifications, stats):
            for clsf in classifications:
                stats['clsf_total'] += 1
                if clsf.get('standard_refs'):
                    stats['clsf_with_refs'] += 1
                if clsf.get('children'):
                    count_clsf(clsf['children'], stats)

        stats = {
            'name': domain_name,
            'clsf_total': 0,
            'clsf_with_refs': 0,
            'term_total': 0,
            'term_with_refs': 0
        }

        count_clsf(domain.get('classifications', []), stats)

        # Count terms
        for term in domain.get('terms', []):
            stats['term_total'] += 1
            if term.get('standard_refs'):
                stats['term_with_refs'] += 1

        clsf_total += stats['clsf_total']
        clsf_with_refs += stats['clsf_with_refs']
        term_total += stats['term_total']
        term_with_refs += stats['term_with_refs']

        stats['clsf_coverage'] = (stats['clsf_with_refs'] / stats['clsf_total'] * 100) if stats['clsf_total'] > 0 else 0
        stats['term_coverage'] = (stats['term_with_refs'] / stats['term_total'] * 100) if stats['term_total'] > 0 else 0

        domain_stats[domain_code] = stats

    # Print report
    print('=' * 80)
    print('표준 레퍼런스 커버리지 분석')
    print('=' * 80)

    print(f'\n전체:')
    print(f'  분류: {clsf_with_refs}/{clsf_total} ({clsf_with_refs/clsf_total*100:.1f}%)')
    print(f'  용어: {term_with_refs}/{term_total} ({term_with_refs/term_total*100:.1f}%)')

    clsf_needed = int(clsf_total * 0.7) - clsf_with_refs
    term_needed = int(term_total * 0.7) - term_with_refs

    if clsf_needed > 0 or term_needed > 0:
        print(f'\n70% 목표까지:')
        if clsf_needed > 0:
            print(f'  분류: {clsf_needed}개 추가 필요')
        else:
            print(f'  분류: ✅ 달성 ({clsf_with_refs/clsf_total*100:.1f}%)')

        if term_needed > 0:
            print(f'  용어: {term_needed}개 추가 필요')
        else:
            print(f'  용어: ✅ 달성 ({term_with_refs/term_total*100:.1f}%)')

    print(f'\n도메인별 커버리지:')
    print(f"{'코드':<4} {'도메인':<15} {'분류':>15} {'분류%':>8} {'용어':>10} {'용어%':>8}")
    print('-' * 80)

    for code in sorted(domain_stats.keys()):
        stats = domain_stats[code]
        print(f"{code:<4} {stats['name']:<15} "
              f"{stats['clsf_with_refs']:3d}/{stats['clsf_total']:3d} ({stats['clsf_coverage']:5.1f}%)"
              f"    {stats['term_with_refs']:2d}/{stats['term_total']:2d} ({stats['term_coverage']:5.1f}%)")

    # Find domains that need more coverage
    print(f'\n우선 작업 대상 (70% 미달):')
    priority = []
    for code in sorted(domain_stats.keys()):
        stats = domain_stats[code]
        if stats['clsf_coverage'] < 70 or stats['term_coverage'] < 70:
            priority.append((code, stats))

    if priority:
        for code, stats in priority:
            clsf_gap = int(stats['clsf_total'] * 0.7) - stats['clsf_with_refs']
            term_gap = int(stats['term_total'] * 0.7) - stats['term_with_refs']
            print(f"  {code} {stats['name']}: 분류 +{max(0, clsf_gap)}, 용어 +{max(0, term_gap)}")
    else:
        print('  ✅ 모든 도메인 70% 이상 달성!')

if __name__ == '__main__':
    analyze_coverage()
