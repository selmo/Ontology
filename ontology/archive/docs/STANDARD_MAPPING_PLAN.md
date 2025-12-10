# 표준 온톨로지 연계 전략 계획

**작성일:** 2025-12-02
**버전:** 1.0
**대상 표준:** DCAT-AP-KR, FIBO, SKOS, Schema.org

---

## 목차

1. [배경 분석](#1-배경-분석)
2. [전략적 목표](#2-전략적-목표)
3. [단계별 실행 계획](#3-단계별-실행-계획)
4. [예상 산출물](#4-예상-산출물)
5. [추가 고려사항](#5-추가-고려사항)

---

## 1. 배경 분석

### 1.1 현재 MC 온톨로지 구조

- **175개 분류** (MC_CLSF) - 계층적 분류 체계
- **124개 용어** (MC_TERM) - 도메인별 핵심 용어
- **264개 관계** (MC_TERM_REL) - 동의어, 연관, 계층
- **10개 도메인** - data.go.kr 기반 재구성

### 1.2 연계 대상 표준

#### DCAT-AP-KR (Data Catalog Vocabulary - Application Profile for Korea)
- W3C DCAT 2.0 기반 한국형 프로필
- 공공데이터포털 메타데이터 표준
- 주요 개념: Dataset, Distribution, Catalog, DataService, Theme
- 분류 체계(dcat:theme)와 MC_CLSF 매핑 가능
- 공식 사이트: https://www.data.go.kr

#### FIBO (Financial Industry Business Ontology)
- EDM Council 금융 온톨로지 표준
- OWL 2 DL 기반
- 재정금융(06) 도메인과 직접 연계 가능
- 주요 모듈:
  - FND (Foundations) - 기초 개념
  - BE (Business Entities) - 비즈니스 엔티티
  - FBC (Financial Business and Commerce) - 금융 비즈니스
  - IND (Indices and Indicators) - 지표
  - SEC (Securities) - 증권
  - LOAN - 대출
- 공식 사이트: https://spec.edmcouncil.org/fibo/

#### SKOS (Simple Knowledge Organization System)
- W3C 표준 분류체계 표현
- Concept, ConceptScheme, Collection
- 매핑 관계: exactMatch, closeMatch, relatedMatch, broadMatch, narrowMatch

#### Schema.org
- 일반 개념 온톨로지
- 검색엔진 최적화(SEO)
- 의료, 교육, 문화 등 범용 개념

#### 기타 표준
- **Dublin Core** - 기본 메타데이터
- **FOAF** - 조직/사람 표현
- **도메인 특화**: SNOMED-CT(의료), LRMI(교육)

---

## 2. 전략적 목표

### 목표 1: 상호운용성 (Interoperability)
- MC 온톨로지를 국제/국내 표준과 연계
- 공공데이터포털과의 호환성 확보
- 금융 도메인의 글로벌 표준 준수

### 목표 2: 의미적 풍부성 (Semantic Enrichment)
- 표준 온톨로지의 의미 정의 활용
- 추론 가능성 확보
- LOD(Linked Open Data) 생태계 참여

### 목표 3: 확장성 (Scalability)
- 새로운 표준 추가 용이성
- 매핑 관리의 체계화
- 버전 관리 및 변경 추적

---

## 3. 단계별 실행 계획

## Phase 1: 설계 및 모델링 (1-2주)

### 1.1 매핑 데이터 모델 설계

#### 옵션 A: 데이터베이스 테이블 방식

```sql
-- MC_STD_MAPPING (표준 매핑 테이블)
CREATE TABLE MC_STD_MAPPING (
    MAPPING_ID   VARCHAR2(32) PRIMARY KEY,
    STD_TYPE     VARCHAR2(50) NOT NULL,     -- 'DCAT-AP-KR', 'FIBO', 'SKOS', 'DCTERMS'
    MC_ID        VARCHAR2(32) NOT NULL,     -- MC_CLSF_ID 또는 MC_TERM_ID
    MC_TYPE      CHAR(1) NOT NULL,          -- 'C' (분류), 'T' (용어)
    STD_URI      VARCHAR2(500) NOT NULL,    -- 표준 온톨로지 URI
    MAPPING_TYPE VARCHAR2(50),              -- 'exactMatch', 'closeMatch', 'relatedMatch', 'broadMatch', 'narrowMatch'
    CONFIDENCE   NUMBER(3,2),               -- 매핑 신뢰도 0.0-1.0
    NOTES        VARCHAR2(1000),            -- 매핑 근거 및 설명
    CREATED_DT   DATE DEFAULT SYSDATE
);

-- 예시 데이터
INSERT INTO MC_STD_MAPPING VALUES (
    'MAP000001',
    'FIBO',
    'T06010001',
    'T',
    'https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate',
    'exactMatch',
    0.95,
    '한국은행 기준금리는 FIBO의 InterestRate 개념과 정확히 일치',
    SYSDATE
);
```

#### 옵션 B: enhanced_data.py 확장 방식

```python
# enhanced_data_mapping.py

# 분류 매핑
CLASSIFICATION_MAPPINGS = {
    'C06000001': {  # 재정금융
        'dcat-ap-kr': {
            'uri': 'http://www.data.go.kr/theme/ECNM',  # 경제/재정
            'type': 'exactMatch',
            'confidence': 1.0
        },
        'skos': {
            'type': 'skos:Concept',
            'broader': None
        }
    },
    'C06010001': {  # 통화정책
        'fibo': {
            'uri': 'https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/MonetaryAuthority',
            'type': 'relatedMatch',
            'confidence': 0.85
        }
    }
}

# 용어 매핑
TERM_MAPPINGS = {
    'T06010001': {  # 기준금리
        'fibo': {
            'uri': 'https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate',
            'type': 'exactMatch',
            'confidence': 0.95,
            'note': 'Central bank policy rate'
        },
        'schema.org': {
            'uri': 'https://schema.org/interestRate',
            'type': 'closeMatch',
            'confidence': 0.80
        }
    },
    'T06020001': {  # 부동산 PF
        'fibo': {
            'uri': 'https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoan/ProjectFinancing',
            'type': 'exactMatch',
            'confidence': 0.90
        }
    }
}
```

### 1.2 우선순위 결정

**우선순위 1 (High Priority)**
- ✅ SKOS 매핑 - 모든 분류/용어
- ✅ DCAT-AP-KR 매핑 - MC_CLSF (분류 체계)
- ✅ FIBO 매핑 - 06 재정금융 도메인

**우선순위 2 (Medium Priority)**
- Dublin Core 매핑 - 메타데이터 속성
- Schema.org 매핑 - 일반 개념 (의료, 교육, 문화 등)

**우선순위 3 (Low Priority)**
- FOAF 매핑 - 조직/기관 개념
- 도메인 특화 온톨로지 (의료: SNOMED-CT, 교육: LRMI 등)

---

## Phase 2: 매핑 데이터 정의 (2-3주)

### 2.1 SKOS 매핑 (전체)

```turtle
@prefix mc: <http://mc.ontology.kr/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

# ConceptScheme (분류 체계)
mc:scheme a skos:ConceptScheme ;
    skos:prefLabel "MC 분류·용어 통합 체계"@ko ;
    skos:prefLabel "MC Classification and Terminology System"@en ;
    dct:created "2024-11-30" ;
    dct:modified "2025-12-01" .

# 분류를 Concept으로
mc:C06000001 a skos:Concept ;
    skos:prefLabel "재정금융"@ko ;
    skos:prefLabel "Finance"@en ;
    skos:definition "금융 부문 정책 및 제도..."@ko ;
    skos:inScheme mc:scheme ;
    skos:topConceptOf mc:scheme .

mc:C06010001 a skos:Concept ;
    skos:prefLabel "통화정책"@ko ;
    skos:broader mc:C06000001 ;
    skos:inScheme mc:scheme .

# 용어를 Concept으로
mc:T06010001 a skos:Concept ;
    skos:prefLabel "기준금리"@ko ;
    skos:prefLabel "Base Rate"@en ;
    skos:altLabel "정책금리"@ko ;
    skos:altLabel "Base Rate"@en ;
    skos:definition "중앙은행이 금융기관과 거래할 때 적용하는 정책금리"@ko ;
    skos:broader mc:C06010001 ;
    skos:related mc:T06010002, mc:T06010003 .

# 동의어는 altLabel로
mc:T03010002 a skos:Concept ;
    skos:prefLabel "대장암"@ko ;
    skos:altLabel "결장암"@ko ;
    skos:altLabel "직장암"@ko ;
    skos:altLabel "CRC"@en .
```

### 2.2 DCAT-AP-KR 매핑 (분류 → Theme)

```python
DCAT_THEME_MAPPING = {
    'C01000001': 'http://www.data.go.kr/theme/ADMN',  # 행정
    'C02000001': 'http://www.data.go.kr/theme/EDUC',  # 교육
    'C03000001': 'http://www.data.go.kr/theme/HLTH',  # 보건의료
    'C04000001': 'http://www.data.go.kr/theme/WLFR',  # 사회복지
    'C05000001': 'http://www.data.go.kr/theme/LAWS',  # 법률
    'C06000001': 'http://www.data.go.kr/theme/ECNM',  # 재정금융
    'C07000001': 'http://www.data.go.kr/theme/INDU',  # 산업경제
    'C08000001': 'http://www.data.go.kr/theme/SAFE',  # 재난안전
    'C09000001': 'http://www.data.go.kr/theme/CULT',  # 문화관광
    'C10000001': 'http://www.data.go.kr/theme/ENVR',  # 환경기상
}
```

### 2.3 FIBO 매핑 (재정금융 도메인)

```python
FIBO_MAPPINGS = {
    # 통화정책
    'T06010001': {  # 기준금리
        'class': 'fibo-fnd-acc-cur:InterestRate',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate',
        'type': 'exactMatch',
        'confidence': 0.95
    },
    'T06010002': {  # 금융중개지원대출
        'class': 'fibo-loan-ln:BankLoan',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/Loans/BankLoan',
        'type': 'closeMatch',
        'confidence': 0.80
    },
    'T06010003': {  # 공개시장운영
        'class': 'fibo-fbc-fct-mkt:OpenMarketOperation',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/Markets/OpenMarketOperation',
        'type': 'exactMatch',
        'confidence': 0.90
    },

    # 금융안정
    'T06020001': {  # 부동산 PF
        'class': 'fibo-loan-reln:ProjectFinancing',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/LOAN/RealEstateLoan/ProjectFinancing',
        'type': 'exactMatch',
        'confidence': 0.90
    },
    'T06020002': {  # 가계부채
        'class': 'fibo-loan-ln:HouseholdDebt',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/HouseholdDebt',
        'type': 'exactMatch',
        'confidence': 0.85
    },

    # 핀테크
    'T06040001': {  # 핀테크
        'class': 'fibo-fbc-fct-fse:FinancialServiceProvider',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/FBC/FunctionalEntities/FinancialServicesEntities/FinancialServiceProvider',
        'type': 'relatedMatch',
        'confidence': 0.70
    },

    # 자본시장
    'T06050001': {  # 퇴직연금
        'class': 'fibo-sec-sec:PensionPlan',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/Securitization/PensionPlan',
        'type': 'closeMatch',
        'confidence': 0.75
    },

    # 녹색금융
    'T06080001': {  # 녹색금융
        'class': 'fibo-loan-ln:GreenBond',
        'uri': 'https://spec.edmcouncil.org/fibo/ontology/LOAN/LoansGeneral/GreenBond',
        'type': 'relatedMatch',
        'confidence': 0.70
    }
}
```

---

## Phase 3: 구현 (2-3주)

### 3.1 파일 구조

```
ontology/
├── enhanced_data.py                # 기존
├── enhanced_data_mapping.py        # 신규: 표준 매핑 정의
├── build_enhanced_json.py          # 수정: 매핑 포함
├── generate.py                     # 수정: RDF 출력 추가
├── generate_rdf.py                 # 신규: RDF/Turtle 생성
├── context.json                    # 수정: mappings 필드 추가
├── context.ttl                     # 신규: Turtle 출력
├── context_skos.ttl                # 신규: SKOS 전용
├── mc_std_mapping_generated.sql    # 신규: 매핑 SQL
└── validate_mappings.py            # 신규: 매핑 검증
```

### 3.2 context.json 스키마 확장

```json
{
  "metadata": {
    "version": "2.1.0",
    "last_updated": "2025-12-01"
  },
  "domains": [
    {
      "code": "06",
      "name_ko": "재정금융",
      "classifications": [
        {
          "id": "C06010001",
          "name": "통화정책",
          "mappings": {
            "fibo": {
              "uri": "https://spec.edmcouncil.org/fibo/ontology/FBC/...",
              "type": "relatedMatch",
              "confidence": 0.85
            },
            "skos": {
              "type": "skos:Concept"
            }
          }
        }
      ],
      "terms": [
        {
          "id": "T06010001",
          "name_ko": "기준금리",
          "mappings": {
            "fibo": {
              "uri": "https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/CurrencyAmount/InterestRate",
              "type": "exactMatch",
              "confidence": 0.95
            },
            "schema.org": {
              "uri": "https://schema.org/interestRate",
              "type": "closeMatch",
              "confidence": 0.80
            }
          }
        }
      ]
    }
  ]
}
```

### 3.3 RDF/Turtle 생성기

```python
# generate_rdf.py
#!/usr/bin/env python3
"""
RDF/Turtle 형식 생성
- SKOS ConceptScheme
- 표준 온톨로지 매핑
"""

import json
from typing import List, Dict

def generate_turtle(data: Dict) -> str:
    """Generate RDF Turtle format"""
    lines = []

    # Prefixes
    lines.append("@prefix mc: <http://mc.ontology.kr/> .")
    lines.append("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .")
    lines.append("@prefix dcat: <http://www.w3.org/ns/dcat#> .")
    lines.append("@prefix fibo-fnd: <https://spec.edmcouncil.org/fibo/ontology/FND/> .")
    lines.append("@prefix dct: <http://purl.org/dc/terms/> .")
    lines.append("@prefix owl: <http://www.w3.org/2002/07/owl#> .")
    lines.append("")

    # ConceptScheme
    lines.append("mc:scheme a skos:ConceptScheme ;")
    lines.append('    skos:prefLabel "MC 분류·용어 통합 체계"@ko ;')
    lines.append('    skos:prefLabel "MC Classification and Terminology System"@en ;')
    lines.append('    dct:created "2024-11-30" ;')
    lines.append('    dct:modified "2025-12-01" ;')
    lines.append('    dct:hasVersion "2.1.0" .')
    lines.append("")

    # Classifications as SKOS Concepts
    for domain in data['domains']:
        for clsf in flatten_classifications(domain['classifications']):
            lines.append(f"mc:{clsf['id']} a skos:Concept ;")
            lines.append(f'    skos:prefLabel "{clsf["name"]}"@ko ;')
            lines.append(f'    skos:definition "{escape_turtle(clsf["description"])}"@ko ;')

            if clsf.get('parent_id'):
                lines.append(f"    skos:broader mc:{clsf['parent_id']} ;")
            else:
                lines.append("    skos:topConceptOf mc:scheme ;")

            # Standard mappings
            if clsf.get('mappings'):
                for std, mapping in clsf['mappings'].items():
                    if std == 'fibo':
                        lines.append(f'    skos:{mapping["type"]} <{mapping["uri"]}> ;')
                    elif std == 'dcat-ap-kr':
                        lines.append(f'    dcat:theme <{mapping["uri"]}> ;')

            lines.append("    skos:inScheme mc:scheme .")
            lines.append("")

    # Terms as SKOS Concepts
    for domain in data['domains']:
        for term in flatten_terms(domain['terms']):
            lines.append(f"mc:{term['id']} a skos:Concept ;")
            lines.append(f'    skos:prefLabel "{term["name_ko"]}"@ko ;')
            lines.append(f'    skos:prefLabel "{term["name_en"]}"@en ;')

            if term.get('acronym'):
                lines.append(f'    skos:notation "{term["acronym"]}" ;')

            if term.get('description'):
                lines.append(f'    skos:definition "{escape_turtle(term["description"])}"@ko ;')

            # Synonyms as altLabel
            if term.get('synonyms'):
                for syn in term['synonyms']:
                    lines.append(f'    skos:altLabel "{syn}" ;')

            # Related terms
            if term.get('related_terms'):
                for rel_id in term['related_terms']:
                    lines.append(f"    skos:related mc:{rel_id} ;")

            # Mappings
            if term.get('mappings'):
                for std, mapping in term['mappings'].items():
                    if std == 'fibo':
                        lines.append(f'    skos:{mapping["type"]} <{mapping["uri"]}> ;')
                    elif std == 'schema.org':
                        lines.append(f'    skos:{mapping["type"]} <{mapping["uri"]}> ;')

            lines.append("    skos:inScheme mc:scheme .")
            lines.append("")

    return '\n'.join(lines)

def escape_turtle(text: str) -> str:
    """Escape special characters for Turtle"""
    return text.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n')

def flatten_classifications(items: List[Dict], result: List[Dict] = None) -> List[Dict]:
    """Flatten hierarchical classifications"""
    if result is None:
        result = []
    for item in items:
        result.append(item)
        if item.get('children'):
            flatten_classifications(item['children'], result)
    return result

def flatten_terms(items: List[Dict], result: List[Dict] = None) -> List[Dict]:
    """Flatten hierarchical terms"""
    if result is None:
        result = []
    for item in items:
        result.append(item)
        if item.get('children'):
            flatten_terms(item['children'], result)
    return result
```

### 3.4 매핑 SQL 생성

```python
def generate_mc_std_mapping_sql(data: Dict) -> str:
    """Generate mc_std_mapping.sql"""
    lines = []
    lines.append("-- MC_STD_MAPPING 표준 매핑 테이블 INSERT 문")
    lines.append(f"-- Generated: {data['metadata']['last_updated']}")
    lines.append("")

    mapping_id = 1
    for domain in data['domains']:
        # Classifications
        for clsf in flatten_classifications(domain['classifications']):
            if clsf.get('mappings'):
                for std_type, mapping in clsf['mappings'].items():
                    uri = mapping['uri']
                    map_type = mapping.get('type', 'relatedMatch')
                    confidence = mapping.get('confidence', 1.0)
                    notes = mapping.get('note', '').replace("'", "''")

                    lines.append(
                        f"INSERT INTO MC_STD_MAPPING (MAPPING_ID, STD_TYPE, MC_ID, MC_TYPE, "
                        f"STD_URI, MAPPING_TYPE, CONFIDENCE, NOTES) "
                        f"VALUES ('MAP{mapping_id:06d}', '{std_type.upper()}', '{clsf['id']}', 'C', "
                        f"'{uri}', '{map_type}', {confidence}, '{notes}');"
                    )
                    mapping_id += 1

        # Terms
        for term in flatten_terms(domain['terms']):
            if term.get('mappings'):
                for std_type, mapping in term['mappings'].items():
                    uri = mapping['uri']
                    map_type = mapping.get('type', 'relatedMatch')
                    confidence = mapping.get('confidence', 1.0)
                    notes = mapping.get('note', '').replace("'", "''")

                    lines.append(
                        f"INSERT INTO MC_STD_MAPPING (MAPPING_ID, STD_TYPE, MC_ID, MC_TYPE, "
                        f"STD_URI, MAPPING_TYPE, CONFIDENCE, NOTES) "
                        f"VALUES ('MAP{mapping_id:06d}', '{std_type.upper()}', '{term['id']}', 'T', "
                        f"'{uri}', '{map_type}', {confidence}, '{notes}');"
                    )
                    mapping_id += 1

        lines.append("")

    return '\n'.join(lines)
```

---

## Phase 4: 검증 및 테스트 (1주)

### 4.1 매핑 검증 스크립트

```python
# validate_mappings.py
#!/usr/bin/env python3
"""
표준 매핑 검증
"""

import json
import re
from urllib.parse import urlparse

def validate_mappings(data: dict):
    """Validate standard mappings"""
    errors = []
    warnings = []
    info = []

    valid_mapping_types = [
        'exactMatch', 'closeMatch', 'relatedMatch',
        'broadMatch', 'narrowMatch'
    ]

    # URI 형식 검증
    for domain in data['domains']:
        for item in flatten_all(domain):
            if item.get('mappings'):
                for std, mapping in item['mappings'].items():
                    item_id = item['id']

                    # URI 형식 검증
                    if 'uri' in mapping:
                        uri = mapping['uri']
                        if not uri.startswith('http'):
                            errors.append(f"{item_id}: Invalid URI {uri}")
                        else:
                            # URL 파싱
                            parsed = urlparse(uri)
                            if not parsed.scheme or not parsed.netloc:
                                errors.append(f"{item_id}: Malformed URI {uri}")

                    # 매핑 타입 검증
                    if 'type' in mapping:
                        if mapping['type'] not in valid_mapping_types:
                            errors.append(
                                f"{item_id}: Invalid mapping type '{mapping['type']}'. "
                                f"Must be one of {valid_mapping_types}"
                            )

                    # 신뢰도 범위
                    if 'confidence' in mapping:
                        conf = mapping['confidence']
                        if not isinstance(conf, (int, float)):
                            errors.append(f"{item_id}: Confidence must be numeric")
                        elif not 0 <= conf <= 1:
                            warnings.append(
                                f"{item_id}: Confidence {conf} out of range [0.0, 1.0]"
                            )
                        elif conf < 0.5:
                            warnings.append(
                                f"{item_id}: Low confidence {conf} for {std} mapping"
                            )

                    # 표준별 URI 패턴 검증
                    if std == 'fibo' and 'uri' in mapping:
                        if 'edmcouncil.org/fibo' not in mapping['uri']:
                            warnings.append(
                                f"{item_id}: FIBO URI should contain 'edmcouncil.org/fibo'"
                            )
                    elif std == 'dcat-ap-kr' and 'uri' in mapping:
                        if 'data.go.kr' not in mapping['uri']:
                            warnings.append(
                                f"{item_id}: DCAT-AP-KR URI should contain 'data.go.kr'"
                            )

    # 통계
    total_mappings = 0
    by_standard = {}
    for domain in data['domains']:
        for item in flatten_all(domain):
            if item.get('mappings'):
                total_mappings += len(item['mappings'])
                for std in item['mappings'].keys():
                    by_standard[std] = by_standard.get(std, 0) + 1

    info.append(f"Total mappings: {total_mappings}")
    for std, count in sorted(by_standard.items()):
        info.append(f"  {std}: {count} mappings")

    return errors, warnings, info

def flatten_all(domain: dict):
    """Flatten all classifications and terms"""
    items = []
    items.extend(flatten_classifications(domain.get('classifications', [])))
    items.extend(flatten_terms(domain.get('terms', [])))
    return items

def flatten_classifications(items, result=None):
    if result is None:
        result = []
    for item in items:
        result.append(item)
        if item.get('children'):
            flatten_classifications(item['children'], result)
    return result

def flatten_terms(items, result=None):
    if result is None:
        result = []
    for item in items:
        result.append(item)
        if item.get('children'):
            flatten_terms(item['children'], result)
    return result

if __name__ == '__main__':
    with open('context.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    errors, warnings, info = validate_mappings(data)

    print("=" * 60)
    print("표준 매핑 검증 결과")
    print("=" * 60)
    print()

    if info:
        print("[정보]")
        for msg in info:
            print(f"ℹ️  INFO: {msg}")
        print()

    if warnings:
        print("[경고]")
        for msg in warnings:
            print(f"⚠️  WARNING: {msg}")
        print()

    if errors:
        print("[오류]")
        for msg in errors:
            print(f"❌ ERROR: {msg}")
        print()

    if not errors and not warnings:
        print("✅ 모든 검증 통과!")

    print("=" * 60)
    print(f"총계: {len(errors)} 오류, {len(warnings)} 경고, {len(info)} 정보")
    print("=" * 60)
```

### 4.2 SPARQL 쿼리 테스트

```sparql
# 재정금융 도메인의 모든 FIBO 매핑 조회
PREFIX mc: <http://mc.ontology.kr/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX fibo: <https://spec.edmcouncil.org/fibo/ontology/>

SELECT ?mc ?label ?fibo
WHERE {
    ?mc skos:prefLabel ?label ;
        skos:exactMatch ?fibo .
    FILTER(STRSTARTS(STR(?mc), "http://mc.ontology.kr/T06"))
    FILTER(STRSTARTS(STR(?fibo), "https://spec.edmcouncil.org/fibo/"))
}

# 모든 동의어 조회
PREFIX mc: <http://mc.ontology.kr/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>

SELECT ?term ?prefLabel ?altLabel
WHERE {
    ?term skos:prefLabel ?prefLabel ;
          skos:altLabel ?altLabel .
    FILTER(LANG(?prefLabel) = "ko")
}

# DCAT-AP-KR 테마 매핑 조회
PREFIX mc: <http://mc.ontology.kr/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX dcat: <http://www.w3.org/ns/dcat#>

SELECT ?classification ?label ?theme
WHERE {
    ?classification a skos:Concept ;
                    skos:prefLabel ?label ;
                    dcat:theme ?theme .
    FILTER(STRSTARTS(STR(?classification), "http://mc.ontology.kr/C"))
}
```

---

## Phase 5: 문서화 및 배포 (1주)

### 5.1 README 업데이트

추가할 섹션:

```markdown
## 표준 온톨로지 연계

### 지원 표준

1. **SKOS** (Simple Knowledge Organization System)
   - 모든 분류 및 용어를 SKOS Concept으로 표현
   - ConceptScheme: `http://mc.ontology.kr/scheme`

2. **DCAT-AP-KR** (Data Catalog Vocabulary - Korea)
   - 분류 체계(dcat:theme) 매핑
   - 공공데이터포털 호환

3. **FIBO** (Financial Industry Business Ontology)
   - 재정금융(06) 도메인 우선 매핑
   - EDM Council 표준 준수

4. **Schema.org** (계획)
   - 일반 개념 매핑

### 매핑 통계

| 표준 | 분류 | 용어 | 총계 |
|------|------|------|------|
| SKOS | 175 | 124 | 299 |
| DCAT-AP-KR | 10 | 0 | 10 |
| FIBO | 0 | 45 | 45 |

### 네임스페이스

- **MC 온톨로지**: `http://mc.ontology.kr/`
- **SKOS**: `http://www.w3.org/2004/02/skos/core#`
- **DCAT**: `http://www.w3.org/ns/dcat#`
- **FIBO**: `https://spec.edmcouncil.org/fibo/ontology/`

### 출력 파일

- `context.ttl` - 전체 RDF/Turtle
- `context_skos.ttl` - SKOS 전용
- `mc_std_mapping_generated.sql` - 매핑 SQL

### SPARQL 엔드포인트 (계획)

```
http://mc.ontology.kr/sparql
```
```

### 5.2 매핑 가이드 문서

새 문서 `MAPPING_GUIDE.md` 작성

---

## 4. 예상 산출물

### 4.1 SQL 파일
1. `mc_std_mapping_generated.sql` - 표준 매핑 테이블

### 4.2 RDF 파일
1. `context.ttl` - 전체 온톨로지 (MC + 매핑)
2. `context_skos.ttl` - SKOS ConceptScheme
3. `context_dcat.ttl` - DCAT-AP-KR 메타데이터 (선택)
4. `context_fibo.ttl` - FIBO 매핑 (재정금융)

### 4.3 Python 파일
1. `enhanced_data_mapping.py` - 매핑 정의
2. `generate_rdf.py` - RDF/Turtle 생성
3. `validate_mappings.py` - 매핑 검증

### 4.4 문서
1. `MAPPING_GUIDE.md` - 매핑 작성 가이드
2. `STANDARDS.md` - 표준 온톨로지 상세 설명
3. `README.md` - 업데이트

---

## 5. 추가 고려사항

### 5.1 네임스페이스 정책

```
http://mc.ontology.kr/              # MC 기본
http://mc.ontology.kr/class/        # 분류
http://mc.ontology.kr/term/         # 용어
http://mc.ontology.kr/mapping/      # 매핑
http://mc.ontology.kr/scheme        # SKOS ConceptScheme
```

### 5.2 버전 관리

```turtle
mc:scheme dct:hasVersion "2.1.0" ;
    dct:modified "2025-12-01" ;
    owl:versionInfo "Added FIBO mappings for finance domain" ;
    dct:replaces <http://mc.ontology.kr/scheme/2.0> .
```

### 5.3 라이선스 및 저작권

```turtle
mc:scheme dct:license <http://creativecommons.org/licenses/by/4.0/> ;
    dct:rights "Based on data.go.kr classification system" ;
    dct:creator "MC Ontology Team" ;
    dct:publisher "MC Organization" .
```

### 5.4 품질 지표

- **매핑 완성도**: 대상 항목 대비 매핑된 항목 비율
- **매핑 정확도**: 평균 confidence 값
- **표준 준수도**: 표준 URI 패턴 준수율
- **검증 통과율**: 오류 없는 매핑 비율

### 5.5 유지보수 계획

- 분기별 매핑 리뷰
- 표준 온톨로지 버전 업데이트 추적
- 신규 표준 추가 검토
- 커뮤니티 피드백 반영

---

## 6. 타임라인

| Phase | 기간 | 주요 활동 | 산출물 |
|-------|------|-----------|--------|
| Phase 1 | 1-2주 | 설계 및 모델링 | 데이터 모델, 우선순위 |
| Phase 2 | 2-3주 | 매핑 데이터 정의 | enhanced_data_mapping.py |
| Phase 3 | 2-3주 | 구현 | RDF 생성기, SQL 생성 |
| Phase 4 | 1주 | 검증 및 테스트 | 검증 스크립트, SPARQL 쿼리 |
| Phase 5 | 1주 | 문서화 및 배포 | 가이드, README 업데이트 |

**총 예상 기간**: 7-10주

---

## 7. 다음 단계

### 즉시 시작 가능
- Phase 1 (설계) - enhanced_data_mapping.py 구조 설계
- MC_STD_MAPPING 테이블 스키마 작성

### 우선 구현
- SKOS 매핑 (가장 보편적이고 단순)
- DCAT-AP-KR 매핑 (공공데이터포털 호환)

### 단계적 확장
- FIBO 매핑 (재정금융 도메인)
- Schema.org 매핑 (일반 개념)
- 도메인 특화 온톨로지

---

**참고 자료:**
- SKOS: https://www.w3.org/2004/02/skos/
- DCAT-AP: https://www.w3.org/TR/vocab-dcat-2/
- FIBO: https://spec.edmcouncil.org/fibo/
- Schema.org: https://schema.org/
