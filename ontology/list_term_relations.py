#!/usr/bin/env python3
"""
List all term-to-term relationships (RELATED_TO) in the ontology
"""

import json
from collections import defaultdict

def list_term_relations(filepath='ontology.json'):
    """List all related term relationships"""

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Build term ID -> name mapping
    term_map = {}
    related_terms = defaultdict(list)

    for domain in data['domains']:
        for term in domain.get('terms', []):
            term_id = term['id']
            term_name = term['name_ko']
            term_name_en = term.get('name_en', '')
            acronym = term.get('acronym', '')

            # Store term info
            term_map[term_id] = {
                'name_ko': term_name,
                'name_en': term_name_en,
                'acronym': acronym,
                'domain': domain['code'],
                'domain_name': domain['name_ko']
            }

            # Store related terms
            if 'related_terms' in term:
                for related_id in term['related_terms']:
                    related_terms[term_id].append(related_id)

    # Print statistics
    total_relations = sum(len(rels) for rels in related_terms.values())
    terms_with_relations = len(related_terms)

    print("=" * 80)
    print("용어 간 연관 관계 (RELATED_TO)")
    print("=" * 80)
    print(f"\n통계:")
    print(f"  - 연관 관계를 가진 용어 수: {terms_with_relations}")
    print(f"  - 총 연관 관계 수: {total_relations}")
    print(f"  - 평균 연관 용어/용어: {total_relations/terms_with_relations:.2f}" if terms_with_relations > 0 else "")

    # Group by domain
    domain_stats = defaultdict(lambda: {'count': 0, 'relations': []})

    for term_id, related_ids in related_terms.items():
        domain_code = term_map[term_id]['domain']
        domain_stats[domain_code]['count'] += len(related_ids)

        for related_id in related_ids:
            domain_stats[domain_code]['relations'].append({
                'from': term_id,
                'to': related_id
            })

    print(f"\n도메인별 통계:")
    print("-" * 80)
    for domain_code in sorted(domain_stats.keys()):
        stats = domain_stats[domain_code]
        domain_name = term_map[list(related_terms.keys())[0]]['domain_name'] if related_terms else ''
        # Get actual domain name
        for domain in data['domains']:
            if domain['code'] == domain_code:
                domain_name = domain['name_ko']
                break
        print(f"{domain_code}. {domain_name}: {stats['count']}개 관계")

    # Print all relationships
    print("\n" + "=" * 80)
    print("전체 연관 관계 목록")
    print("=" * 80)

    # Sort by domain
    for domain in sorted(data['domains'], key=lambda x: x['code']):
        domain_code = domain['code']
        domain_name = domain['name_ko']

        # Get relations for this domain
        domain_relations = []
        for term_id, related_ids in related_terms.items():
            if term_map[term_id]['domain'] == domain_code:
                for related_id in related_ids:
                    domain_relations.append((term_id, related_id))

        if not domain_relations:
            continue

        print(f"\n{'=' * 80}")
        print(f"{domain_code}. {domain_name} ({len(domain_relations)}개)")
        print('=' * 80)

        for from_id, to_id in domain_relations:
            from_term = term_map[from_id]
            to_term = term_map.get(to_id, {'name_ko': to_id, 'name_en': '', 'acronym': ''})

            from_str = from_term['name_ko']
            if from_term['acronym']:
                from_str += f" [{from_term['acronym']}]"
            if from_term['name_en']:
                from_str += f" | {from_term['name_en']}"

            to_str = to_term['name_ko']
            if to_term.get('acronym'):
                to_str += f" [{to_term['acronym']}]"
            if to_term.get('name_en'):
                to_str += f" | {to_term['name_en']}"

            print(f"  {from_id}: {from_str}")
            print(f"    → {to_id}: {to_str}")
            print()

    # Print matrix view
    print("\n" + "=" * 80)
    print("연관 관계 네트워크 (허브 용어)")
    print("=" * 80)

    # Find terms with most connections
    connection_count = defaultdict(int)
    for term_id, related_ids in related_terms.items():
        connection_count[term_id] += len(related_ids)
        for related_id in related_ids:
            connection_count[related_id] += 1  # Count incoming connections too

    # Sort by connection count
    top_terms = sorted(connection_count.items(), key=lambda x: x[1], reverse=True)[:20]

    print("\n상위 20개 허브 용어 (연결 수 기준):")
    print("-" * 80)
    for i, (term_id, count) in enumerate(top_terms, 1):
        if term_id in term_map:
            term = term_map[term_id]
            print(f"{i:2d}. {term['name_ko']:20s} ({term_id}): {count}개 연결")

    return related_terms, term_map


if __name__ == '__main__':
    list_term_relations()
