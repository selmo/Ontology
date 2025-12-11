#!/usr/bin/env python3
"""
Apply Close Match suggestions to ontology.json
Auto-apply high confidence (0.9+) suggestions
"""

import json
from datetime import datetime

def apply_close_matches(suggestions_file='close_match_suggestions.json',
                        ontology_file='ontology.json',
                        confidence_threshold=0.9):
    """Apply close match suggestions"""

    # Load suggestions
    with open(suggestions_file, 'r', encoding='utf-8') as f:
        suggestions = json.load(f)

    # Load ontology
    with open(ontology_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Build term lookup
    term_lookup = {}
    for domain in data['domains']:
        for term in domain.get('terms', []):
            term_lookup[term['id']] = term

    # Apply suggestions
    applied = []
    skipped = []

    for sug in suggestions:
        if sug['confidence'] < confidence_threshold:
            skipped.append(sug)
            continue

        term_id = sug['term_id']
        synonym = sug['synonym']

        if term_id not in term_lookup:
            print(f"  ! Term {term_id} not found")
            continue

        term = term_lookup[term_id]
        synonyms = term.get('synonyms', {})

        if not isinstance(synonyms, dict):
            continue

        related = synonyms.get('related', [])
        close = synonyms.get('close', [])

        # Move from related to close
        if synonym in related:
            related.remove(synonym)
            close.append(synonym)
            synonyms['related'] = related
            synonyms['close'] = close

            applied.append({
                'term_id': term_id,
                'term': sug['term'],
                'synonym': synonym,
                'confidence': sug['confidence']
            })

    # Update metadata
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')

    # Save
    with open(ontology_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return applied, skipped

def print_report(applied, skipped, threshold):
    """Print report"""

    print("=" * 80)
    print("Close Match 적용 결과")
    print("=" * 80)

    print(f"\nConfidence threshold: {threshold}")
    print(f"적용됨: {len(applied)}개")
    print(f"보류됨: {len(skipped)}개")

    if applied:
        print(f"\n적용된 Close Match ({len(applied)}개):")
        print("-" * 80)
        print(f"{'Term ID':<12} {'Term':30s} {'→':3s} {'Synonym':30s} {'Confidence':>10s}")
        print("-" * 80)

        for item in applied:
            print(f"{item['term_id']:<12} {item['term']:30s} {'→':3s} {item['synonym']:30s} {item['confidence']:>10.2f}")

    if skipped:
        print(f"\n보류된 후보 ({len(skipped)}개) - 수동 검토 필요:")
        print("-" * 80)
        print(f"  Confidence 0.8-0.9: 검토 추천")
        print(f"  Confidence 0.7-0.8: 참고")
        print(f"\n  close_match_suggestions.json 참조")

    print(f"\n✅ 완료: {len(applied)}개 Close Match 적용")

if __name__ == '__main__':
    applied, skipped = apply_close_matches(confidence_threshold=0.9)
    print_report(applied, skipped, 0.9)
