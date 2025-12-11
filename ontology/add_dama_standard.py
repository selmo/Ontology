#!/usr/bin/env python3
"""
DAMA-DMBOK 표준을 standards registry에 추가
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


def add_dama_standard():
    """DAMA-DMBOK 표준 추가"""

    print("=" * 80)
    print("DAMA-DMBOK 표준 등록")
    print("=" * 80)
    print()

    ontology = load_json('ontology.json')

    # DAMA-DMBOK 표준 정의
    dama_standard = {
        "id": "STD-DAMA",
        "code": "DAMA-DMBOK",
        "name_ko": "DAMA-DMBOK",
        "name_en": "Data Management Body of Knowledge",
        "type": "INTERNATIONAL",
        "scope": "ONTOLOGY",
        "organization": "DAMA International",
        "version": "2.0 (2017)",
        "uri": "https://www.dama.org/cpages/body-of-knowledge",
        "description": "데이터 관리 전문가를 위한 11개 지식 영역 체계. 데이터 거버넌스, 아키텍처, 품질, 보안, 통합, MDM, DW/BI, 메타데이터 등 포괄."
    }

    # Check if already exists
    existing = False
    for std in ontology['standards']['registry']:
        if std['id'] == 'STD-DAMA':
            existing = True
            print("⚠️  STD-DAMA가 이미 존재합니다.")
            break

    if not existing:
        ontology['standards']['registry'].append(dama_standard)
        ontology['standards']['count'] = len(ontology['standards']['registry'])

        print(f"✅ DAMA-DMBOK 표준 추가 완료")
        print(f"   - ID: {dama_standard['id']}")
        print(f"   - 코드: {dama_standard['code']}")
        print(f"   - 유형: {dama_standard['type']}")
        print(f"   - 범위: {dama_standard['scope']}")
        print(f"   - 조직: {dama_standard['organization']}")
        print(f"   - 버전: {dama_standard['version']}")
        print()
        print(f"총 표준 수: {ontology['standards']['count']}개")
        print()

        save_json('ontology.json', ontology)

    print()
    print("=" * 80)
    print("✅ 완료")
    print("=" * 80)


if __name__ == '__main__':
    add_dama_standard()
