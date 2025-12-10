#!/usr/bin/env python3
"""
Analyze all relationship types in the ontology
"""

import json
import re

def analyze_cypher_relationships(cypher_file='generated/ontology.cypher'):
    """Analyze relationships from Cypher file"""

    with open(cypher_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all relationship patterns
    relationships = {
        'PARENT_OF': {'count': 0, 'examples': []},
        'BELONGS_TO': {'count': 0, 'examples': []},
        'SYNONYM_OF': {'count': 0, 'examples': []},
        'RELATED_TO': {'count': 0, 'examples': []}
    }

    # Count PARENT_OF (Classification and Term hierarchies)
    parent_of_pattern = r'CREATE \(p.*?\)-\[:PARENT_OF\]->\(c.*?\);'
    parent_of_matches = re.findall(parent_of_pattern, content)
    relationships['PARENT_OF']['count'] = len(parent_of_matches)
    relationships['PARENT_OF']['examples'] = parent_of_matches[:3]

    # Count BELONGS_TO (Term -> Classification)
    belongs_to_pattern = r'MATCH \(t:Term.*?\), \(c:Classification.*?\) CREATE \(t\)-\[:BELONGS_TO\]->\(c\);'
    belongs_to_matches = re.findall(belongs_to_pattern, content)
    relationships['BELONGS_TO']['count'] = len(belongs_to_matches)
    relationships['BELONGS_TO']['examples'] = belongs_to_matches[:3]

    # Count SYNONYM_OF (Term -> Synonym)
    synonym_of_pattern = r'MATCH \(t:Term.*?\), \(s:Synonym.*?\) CREATE \(t\)-\[:SYNONYM_OF\]->\(s\);'
    synonym_of_matches = re.findall(synonym_of_pattern, content)
    relationships['SYNONYM_OF']['count'] = len(synonym_of_matches)
    relationships['SYNONYM_OF']['examples'] = synonym_of_matches[:3]

    # Count RELATED_TO (Term -> Term)
    related_to_pattern = r'MATCH \(t1:Term.*?\), \(t2:Term.*?\) CREATE \(t1\)-\[:RELATED_TO\]->\(t2\);'
    related_to_matches = re.findall(related_to_pattern, content)
    relationships['RELATED_TO']['count'] = len(related_to_matches)
    relationships['RELATED_TO']['examples'] = related_to_matches[:3]

    return relationships


def analyze_json_relationships(json_file='ontology.json'):
    """Analyze relationships from JSON file"""

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    stats = {
        'terms': {
            'total': 0,
            'with_synonyms': 0,
            'with_related': 0,
            'with_belongs_to': 0
        },
        'relationships': {
            'synonyms': 0,
            'related_terms': 0,
            'belongs_to': 0
        }
    }

    for domain in data['domains']:
        for term in domain.get('terms', []):
            stats['terms']['total'] += 1

            # Count synonyms
            if 'synonyms' in term and term['synonyms']:
                stats['terms']['with_synonyms'] += 1
                stats['relationships']['synonyms'] += len(term['synonyms'])

            # Count related terms
            if 'related_terms' in term and term['related_terms']:
                stats['terms']['with_related'] += 1
                stats['relationships']['related_terms'] += len(term['related_terms'])

            # Count belongs_to (classification_id)
            if 'classification_id' in term:
                stats['terms']['with_belongs_to'] += 1
                stats['relationships']['belongs_to'] += 1

    return stats


def print_report():
    """Print comprehensive relationship report"""

    print("=" * 80)
    print("온톨로지 Relationship 타입 분석")
    print("=" * 80)

    # Analyze Cypher
    cypher_rels = analyze_cypher_relationships()

    # Analyze JSON
    json_stats = analyze_json_relationships()

    print("\n## 1. Relationship 타입 목록")
    print("-" * 80)

    relationship_types = [
        {
            'type': 'PARENT_OF',
            'source': 'Classification/Term',
            'target': 'Classification/Term',
            'description': '계층 구조 관계 (상위→하위)',
            'count': cypher_rels['PARENT_OF']['count'],
            'bidirectional': False,
            'properties': None
        },
        {
            'type': 'BELONGS_TO',
            'source': 'Term',
            'target': 'Classification',
            'description': '용어가 분류에 속함',
            'count': cypher_rels['BELONGS_TO']['count'],
            'bidirectional': False,
            'properties': None
        },
        {
            'type': 'SYNONYM_OF',
            'source': 'Term',
            'target': 'Synonym',
            'description': '용어의 동의어',
            'count': cypher_rels['SYNONYM_OF']['count'],
            'bidirectional': False,
            'properties': None
        },
        {
            'type': 'RELATED_TO',
            'source': 'Term',
            'target': 'Term',
            'description': '용어 간 연관 관계',
            'count': cypher_rels['RELATED_TO']['count'],
            'bidirectional': True,
            'properties': None
        }
    ]

    for i, rel in enumerate(relationship_types, 1):
        print(f"\n### {i}. {rel['type']}")
        print(f"   - Source: {rel['source']}")
        print(f"   - Target: {rel['target']}")
        print(f"   - Description: {rel['description']}")
        print(f"   - Count: {rel['count']:,}")
        print(f"   - Bidirectional: {'Yes' if rel['bidirectional'] else 'No'}")
        print(f"   - Properties: {rel['properties'] if rel['properties'] else 'None'}")

    print("\n\n## 2. Relationship 통계")
    print("-" * 80)

    total_relationships = sum(r['count'] for r in relationship_types)

    print(f"\n전체 관계 수: {total_relationships:,}")
    print("\n타입별 분포:")
    for rel in sorted(relationship_types, key=lambda x: x['count'], reverse=True):
        percentage = (rel['count'] / total_relationships * 100) if total_relationships > 0 else 0
        print(f"  - {rel['type']:15s}: {rel['count']:4,} ({percentage:5.1f}%)")

    print("\n\n## 3. 용어(Term) 관계 상세")
    print("-" * 80)

    print(f"\n총 용어 수: {json_stats['terms']['total']}")
    print(f"\n관계 보유 현황:")
    print(f"  - 동의어 보유: {json_stats['terms']['with_synonyms']} / {json_stats['terms']['total']} "
          f"({json_stats['terms']['with_synonyms']/json_stats['terms']['total']*100:.1f}%)")
    print(f"  - 연관 용어 보유: {json_stats['terms']['with_related']} / {json_stats['terms']['total']} "
          f"({json_stats['terms']['with_related']/json_stats['terms']['total']*100:.1f}%)")
    print(f"  - 분류 연결: {json_stats['terms']['with_belongs_to']} / {json_stats['terms']['total']} "
          f"({json_stats['terms']['with_belongs_to']/json_stats['terms']['total']*100:.1f}%)")

    print(f"\n관계 총계:")
    print(f"  - 동의어: {json_stats['relationships']['synonyms']:,}개")
    print(f"  - 연관 용어: {json_stats['relationships']['related_terms']:,}개")
    print(f"  - 분류 연결: {json_stats['relationships']['belongs_to']:,}개")

    print("\n\n## 4. Cypher 쿼리 예시")
    print("-" * 80)

    examples = [
        {
            'title': 'PARENT_OF - 분류 계층 구조 조회',
            'query': '''MATCH path = (root:Classification {id: 'C01000001'})-[:PARENT_OF*]->(child)
RETURN path
LIMIT 10;'''
        },
        {
            'title': 'BELONGS_TO - 용어가 속한 분류 찾기',
            'query': '''MATCH (t:Term {name_ko: '인공지능'})-[:BELONGS_TO]->(c:Classification)
RETURN t.name_ko AS term, c.name AS classification;'''
        },
        {
            'title': 'SYNONYM_OF - 용어의 모든 동의어 조회',
            'query': '''MATCH (t:Term {name_ko: '공공기관'})-[:SYNONYM_OF]->(s:Synonym)
RETURN t.name_ko, collect(s.name) AS synonyms;'''
        },
        {
            'title': 'RELATED_TO - 연관 용어 탐색',
            'query': '''MATCH (t1:Term {name_ko: '의료기관'})-[:RELATED_TO]->(t2:Term)
RETURN t1.name_ko, t2.name_ko;'''
        },
        {
            'title': '복합 쿼리 - 용어의 모든 관계',
            'query': '''MATCH (t:Term {name_ko: '국가예산'})
OPTIONAL MATCH (t)-[:BELONGS_TO]->(c:Classification)
OPTIONAL MATCH (t)-[:SYNONYM_OF]->(s:Synonym)
OPTIONAL MATCH (t)-[:RELATED_TO]->(r:Term)
RETURN t.name_ko,
       c.name AS classification,
       collect(DISTINCT s.name) AS synonyms,
       collect(DISTINCT r.name_ko) AS related_terms;'''
        }
    ]

    for i, example in enumerate(examples, 1):
        print(f"\n### 예시 {i}: {example['title']}")
        print("```cypher")
        print(example['query'])
        print("```")

    print("\n\n## 5. 그래프 스키마")
    print("-" * 80)
    print("""
노드 타입:
  - Classification (377개): 분류 노드
  - Term (222개): 용어 노드
  - Synonym (485개): 동의어 노드

관계 타입:
  ┌─────────────┐
  │Classification│
  └──────┬──────┘
         │ :PARENT_OF (376개)
         ↓
  ┌─────────────┐
  │Classification│
  └─────────────┘
         ↑
         │ :BELONGS_TO (221개)
         │
    ┌────┴────┐
    │  Term   │──→ :SYNONYM_OF (552개) ──→ ┌─────────┐
    └────┬────┘                           │ Synonym │
         │                                └─────────┘
         │ :RELATED_TO (83개)
         ↓
    ┌────────┐
    │  Term  │
    └────────┘

계층 구조:
  - ROOT Classification → 12 Domain Classifications
  - Each Domain → Multiple Category Classifications
  - Each Category → Multiple Sub-classifications
  - ROOT Term → 221 Domain Terms
""")


if __name__ == '__main__':
    print_report()
