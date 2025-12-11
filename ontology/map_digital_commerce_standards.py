#!/usr/bin/env python3
"""
디지털커머스 도메인에 GS1, Schema.org 표준 매핑
v3.14.0: 미사용 표준 활용
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


def map_standards():
    """디지털커머스 표준 매핑"""

    print("=" * 80)
    print("디지털커머스 도메인 표준 매핑")
    print("=" * 80)
    print()

    ontology = load_json('ontology.json')

    # Find digital commerce domain (code 08)
    domain_08 = None
    for domain in ontology['domains']:
        if domain['code'] == '08':
            domain_08 = domain
            break

    if not domain_08:
        print("❌ 디지털커머스 도메인을 찾을 수 없습니다.")
        return

    print(f"현재 용어 수: {len(domain_08['terms'])}개")
    print(f"현재 primary_standards: {domain_08.get('primary_standards', [])}")
    print()

    # Add GS1 and Schema.org to primary standards
    if 'primary_standards' not in domain_08:
        domain_08['primary_standards'] = []

    if 'STD-GS1' not in domain_08['primary_standards']:
        domain_08['primary_standards'].append('STD-GS1')

    if 'STD-SCHEMA' not in domain_08['primary_standards']:
        domain_08['primary_standards'].append('STD-SCHEMA')

    print(f"✅ Primary standards 추가: {domain_08['primary_standards']}")
    print()

    # Map standards to relevant terms (실제 용어 기준)
    mappings = [
        # 이커머스 플랫폼
        {
            "term_name": "이커머스 플랫폼",
            "standards": [
                {
                    "standard_id": "STD-GS1",
                    "external_id": "eCommerce",
                    "external_name": "GS1 eCommerce Standards",
                    "match_type": "BROAD_MATCH",
                    "confidence": 0.85,
                    "note": "글로벌 유통·물류·전자상거래 표준"
                },
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "WebSite, WebPage",
                    "external_name": "Schema.org WebSite/WebPage",
                    "match_type": "BROAD_MATCH",
                    "confidence": 0.80,
                    "note": "웹 구조화 데이터 표준"
                }
            ]
        },
        # D2C
        {
            "term_name": "D2C",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "Product, Offer",
                    "external_name": "Schema.org Product/Offer",
                    "match_type": "RELATED_MATCH",
                    "confidence": 0.75
                }
            ]
        },
        # 간편결제
        {
            "term_name": "간편결제",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "PaymentMethod",
                    "external_name": "Schema.org PaymentMethod",
                    "match_type": "EXACT_MATCH",
                    "confidence": 0.90
                }
            ]
        },
        # BNPL
        {
            "term_name": "BNPL",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "PaymentMethod",
                    "external_name": "Schema.org PaymentMethod",
                    "match_type": "RELATED_MATCH",
                    "confidence": 0.85,
                    "note": "Buy Now Pay Later 결제 방식"
                }
            ]
        },
        # 풀필먼트
        {
            "term_name": "풀필먼트",
            "standards": [
                {
                    "standard_id": "STD-GS1",
                    "external_id": "Logistics",
                    "external_name": "GS1 Logistics Standards",
                    "match_type": "BROAD_MATCH",
                    "confidence": 0.85,
                    "note": "주문처리·재고관리·배송 통합"
                }
            ]
        },
        # 라스트마일
        {
            "term_name": "라스트마일",
            "standards": [
                {
                    "standard_id": "STD-GS1",
                    "external_id": "GLN",
                    "external_name": "Global Location Number",
                    "match_type": "RELATED_MATCH",
                    "confidence": 0.75,
                    "note": "최종 배송지 위치식별"
                }
            ]
        },
        # 라이브커머스
        {
            "term_name": "라이브커머스",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "BroadcastEvent, Product",
                    "external_name": "Schema.org BroadcastEvent/Product",
                    "match_type": "RELATED_MATCH",
                    "confidence": 0.80
                }
            ]
        },
        # 구독경제
        {
            "term_name": "구독경제",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "Subscription",
                    "external_name": "Schema.org Subscription",
                    "match_type": "EXACT_MATCH",
                    "confidence": 0.90
                }
            ]
        },
        # 바코드번호
        {
            "term_name": "바코드번호",
            "standards": [
                {
                    "standard_id": "STD-GS1",
                    "external_id": "GTIN",
                    "external_name": "Global Trade Item Number",
                    "match_type": "EXACT_MATCH",
                    "confidence": 0.95,
                    "note": "GS1 글로벌 상품식별번호 (바코드)"
                }
            ]
        },
        # 주문번호
        {
            "term_name": "주문번호",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "OrderNumber",
                    "external_name": "Schema.org Order.orderNumber",
                    "match_type": "EXACT_MATCH",
                    "confidence": 0.95
                }
            ]
        },
        # 배송지주소
        {
            "term_name": "배송지주소",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "PostalAddress",
                    "external_name": "Schema.org PostalAddress",
                    "match_type": "EXACT_MATCH",
                    "confidence": 0.95
                },
                {
                    "standard_id": "STD-GS1",
                    "external_id": "GLN",
                    "external_name": "Global Location Number",
                    "match_type": "RELATED_MATCH",
                    "confidence": 0.80
                }
            ]
        },
        # 배송비
        {
            "term_name": "배송비",
            "standards": [
                {
                    "standard_id": "STD-SCHEMA",
                    "external_id": "DeliveryChargeSpecification",
                    "external_name": "Schema.org DeliveryChargeSpecification",
                    "match_type": "EXACT_MATCH",
                    "confidence": 0.90
                }
            ]
        }
    ]

    # Apply mappings
    mapped_count = 0
    ref_count = 0

    for mapping in mappings:
        term_name = mapping["term_name"]
        standards = mapping["standards"]

        # Find term
        for term in domain_08['terms']:
            if term['name_ko'] == term_name:
                if 'standard_refs' not in term:
                    term['standard_refs'] = []

                # Add new references
                for std_ref in standards:
                    # Check if already exists
                    existing = False
                    for existing_ref in term['standard_refs']:
                        if existing_ref['standard_id'] == std_ref['standard_id']:
                            existing = True
                            break

                    if not existing:
                        term['standard_refs'].append(std_ref)
                        ref_count += 1
                        print(f"✅ {term_name} + {std_ref['standard_id']}")

                mapped_count += 1
                break

    print()
    print(f"✅ 총 {mapped_count}개 용어에 {ref_count}개 표준 레퍼런스 추가")
    print()

    # Save
    save_json('ontology.json', ontology)

    print()
    print("=" * 80)
    print("✅ 디지털커머스 표준 매핑 완료")
    print("=" * 80)


if __name__ == '__main__':
    map_standards()
