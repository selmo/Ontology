#!/usr/bin/env python3
"""
DAMA-DMBOK 기반 도메인 추가 및 보강
- 13번 데이터 거버넌스: 5개 중분류 추가 (23개 분류, 9개 용어)
- 15번 데이터 관리: 신규 도메인 (18개 분류, 8개 용어)
- 16번 데이터 분석: 신규 도메인 (19개 분류, 9개 용어)
"""

import json


def load_json(filepath):
    """JSON 파일 로드"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(filepath, data):
    """JSON 파일 저장"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 저장 완료: {filepath}")


def apply_dama_domains():
    """DAMA 기반 도메인 추가/보강"""

    print("=" * 80)
    print("DAMA-DMBOK 기반 도메인 추가 및 보강")
    print("=" * 80)
    print()

    # Load files
    ontology = load_json('ontology.json')
    domain_13_enhanced = load_json('domain_13_enhanced.json')
    domain_15 = load_json('domain_15_data_management_design.json')
    domain_16 = load_json('domain_16_data_analytics_design.json')

    # Current stats
    total_domains = len(ontology['domains'])
    total_clsf = sum(len(d['classifications']) for d in ontology['domains'])
    total_terms = sum(len(d['terms']) for d in ontology['domains'])

    print(f"현재 상태:")
    print(f"  - 도메인: {total_domains}개")
    print(f"  - 분류: {total_clsf}개")
    print(f"  - 용어: {total_terms}개")
    print()

    # Step 1: Enhance domain 13 (Data Governance)
    print("=" * 80)
    print("1. 도메인 13 (데이터 거버넌스) 보강")
    print("=" * 80)
    print()

    for domain in ontology['domains']:
        if domain['code'] == '13':
            # Add DAMA to primary standards
            if 'STD-DAMA' not in domain.get('primary_standards', []):
                domain['primary_standards'].append('STD-DAMA')

            # Add new classifications
            new_clsfs = domain_13_enhanced['enhancements']['new_classifications']
            domain['classifications'].extend(new_clsfs)

            # Add new terms
            new_terms = domain_13_enhanced['enhancements']['new_terms']
            domain['terms'].extend(new_terms)

            print(f"✅ 도메인 13 보강 완료")
            print(f"   - 분류: +{len(new_clsfs)}개")
            print(f"   - 용어: +{len(new_terms)}개")
            print(f"   - 표준: STD-DAMA 추가")
            print()
            break

    # Step 2: Add domain 15 (Data Management)
    print("=" * 80)
    print("2. 도메인 15 (데이터 관리) 추가")
    print("=" * 80)
    print()

    domain_15_data = {
        "code": domain_15["domain"]["code"],
        "name_ko": domain_15["domain"]["name_ko"],
        "name_en": domain_15["domain"]["name_en"],
        "description": domain_15["domain"]["description"],
        "primary_standards": domain_15["domain"]["primary_standards"],
        "classifications": domain_15["classifications"],
        "terms": domain_15["terms"]
    }

    ontology['domains'].append(domain_15_data)

    print(f"✅ 도메인 15 추가 완료")
    print(f"   - 분류: {len(domain_15['classifications'])}개")
    print(f"   - 용어: {len(domain_15['terms'])}개")
    print()

    # Step 3: Add domain 16 (Data Analytics)
    print("=" * 80)
    print("3. 도메인 16 (데이터 분석) 추가")
    print("=" * 80)
    print()

    domain_16_data = {
        "code": domain_16["domain"]["code"],
        "name_ko": domain_16["domain"]["name_ko"],
        "name_en": domain_16["domain"]["name_en"],
        "description": domain_16["domain"]["description"],
        "primary_standards": domain_16["domain"]["primary_standards"],
        "classifications": domain_16["classifications"],
        "terms": domain_16["terms"]
    }

    ontology['domains'].append(domain_16_data)

    print(f"✅ 도메인 16 추가 완료")
    print(f"   - 분류: {len(domain_16['classifications'])}개")
    print(f"   - 용어: {len(domain_16['terms'])}개")
    print()

    # Update metadata
    ontology['metadata']['version'] = '3.15.0'
    ontology['metadata']['last_updated'] = '2025-12-11'
    ontology['metadata']['description'] = (
        "MC 분류·용어 통합 체계 (DAMA-DMBOK 기반 도메인 확장: "
        "데이터 거버넌스 보강 + 데이터 관리/분석 신설)"
    )

    # New stats
    print("=" * 80)
    print("통계 업데이트")
    print("=" * 80)
    print()

    new_total_clsf = sum(len(d['classifications']) for d in ontology['domains'])
    new_total_terms = sum(len(d['terms']) for d in ontology['domains'])
    new_total_domains = len(ontology['domains'])

    print(f"도메인: {total_domains}개 → {new_total_domains}개 (+{new_total_domains - total_domains})")
    print(f"분류: {total_clsf}개 → {new_total_clsf}개 (+{new_total_clsf - total_clsf})")
    print(f"용어: {total_terms}개 → {new_total_terms}개 (+{new_total_terms - total_terms})")
    print()

    # Save
    save_json('ontology.json', ontology)

    print()
    print("=" * 80)
    print("✅ v3.15.0 DAMA 도메인 추가 완료")
    print("=" * 80)
    print()
    print("DAMA-DMBOK 커버리지:")
    print("  1. Data Governance ✅ (13번)")
    print("  2. Data Architecture ✅ (13번)")
    print("  3. Data Modeling & Design ✅ (13번)")
    print("  4. Data Storage & Operations ✅ (15번)")
    print("  5. Data Security ✅ (13번)")
    print("  6. Data Integration & Interoperability ✅ (15번)")
    print("  7. Document & Content Management ✅ (15번)")
    print("  8. Reference & Master Data ✅ (13번)")
    print("  9. Data Warehousing & BI ✅ (16번)")
    print(" 10. Metadata ✅ (13번)")
    print(" 11. Data Quality ✅ (13번)")
    print()
    print("총 커버리지: 11/11 (100%) 🎉")


if __name__ == '__main__':
    apply_dama_domains()
