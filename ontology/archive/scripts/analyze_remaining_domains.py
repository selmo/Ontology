#!/usr/bin/env python3
"""
Analyze 디지털커머스 and 과학기술 domains for standard reference expansion
"""

import json

def analyze_remaining_domains(filepath='ontology.json'):
    """Analyze classifications without standard_refs in target domains"""

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    target_domains = ['08', '11']  # 디지털커머스, 과학기술

    for domain in data['domains']:
        if domain['code'] not in target_domains:
            continue

        print("=" * 80)
        print(f"{domain['code']}. {domain['name_ko']} ({domain['name_en']})")
        print("=" * 80)

        total = 0
        with_refs = 0
        without_refs = []

        def analyze_classifications(classifications, level=0):
            nonlocal total, with_refs

            for clsf in classifications:
                total += 1
                indent = "  " * level

                has_refs = 'standard_refs' in clsf and len(clsf.get('standard_refs', [])) > 0

                if has_refs:
                    with_refs += 1
                    status = "✓"
                    refs = clsf['standard_refs']
                    ref_info = f" [{len(refs)} refs: {', '.join([r['standard_id'] for r in refs])}]"
                else:
                    status = "✗"
                    ref_info = ""
                    without_refs.append({
                        'id': clsf['id'],
                        'name': clsf['name'],
                        'description': clsf.get('description', ''),
                        'level': level
                    })

                print(f"{indent}{status} {clsf['id']}: {clsf['name']}{ref_info}")

                if 'children' in clsf:
                    analyze_classifications(clsf['children'], level + 1)

        analyze_classifications(domain.get('classifications', []))

        print(f"\n통계:")
        print(f"  - 전체 분류: {total}")
        print(f"  - 표준 레퍼런스 보유: {with_refs} ({with_refs/total*100:.1f}%)")
        print(f"  - 표준 레퍼런스 미보유: {len(without_refs)} ({len(without_refs)/total*100:.1f}%)")
        print(f"  - 50% 달성을 위한 필요 매핑 수: {max(0, int(total * 0.5) - with_refs)}")

        print(f"\n표준 레퍼런스 미보유 분류 상세:")
        print("-" * 80)
        for clsf in without_refs:
            indent = "  " * clsf['level']
            desc = f"\n{indent}    설명: {clsf['description']}" if clsf['description'] else ""
            print(f"{indent}{clsf['id']}: {clsf['name']}{desc}")

        print("\n")

if __name__ == '__main__':
    analyze_remaining_domains()
