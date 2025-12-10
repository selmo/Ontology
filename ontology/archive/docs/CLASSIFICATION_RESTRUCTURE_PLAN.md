# 온톨로지 분류체계 재구축 플랜

**작성일:** 2025-12-10
**버전:** Draft 1.0
**목적:** 국제/국내 표준을 반영한 분류체계 전면 재설계

---

## 1. 조사된 표준 체계 요약

### 1.1 국제 표준

| 표준명 | 관리기관 | 특징 | 적용 가능성 |
|--------|----------|------|-------------|
| **SKOS** | W3C | 시소러스/분류체계를 위한 데이터 모델. RDF 기반. broader/narrower 관계 지원 | ★★★ 핵심 적용 |
| **ISO 25964** | ISO | 시소러스 국제 표준. SKOS와 호환. 2레벨(Part 1: 시소러스, Part 2: 상호운용성) | ★★★ 구조 참조 |
| **Dublin Core** | DCMI | 15개 핵심 메타데이터 요소. ISO 15836 표준화 | ★★☆ 메타데이터 적용 |
| **Schema.org** | Google/MS/Yahoo | 827 Types, 1528 Properties. 웹 검색 최적화용 | ★☆☆ 참조용 |
| **UNESCO Thesaurus** | UNESCO | 7개 주제 도메인. SKOS/ISO 25964 준수. 다국어 지원 | ★★☆ 도메인 참조 |
| **OECD FOS** | OECD | 6개 대분류, 42개 소분류. 과학기술 분야 | ★★☆ 과학기술 분야 |

### 1.2 국내 표준

| 표준명 | 관리기관 | 특징 | 적용 가능성 |
|--------|----------|------|-------------|
| **BRM** | 행정안전부/국가기록원 | 정부기능분류체계. 6레벨 구조. 17개 정책분야, 76개 정책영역 | ★★★ 공공행정 적용 |
| **KSIC** | 통계청 | 한국표준산업분류 11차 개정(2024). 5레벨(대-중-소-세-세세) | ★★★ 산업/경제 적용 |
| **KCD** | 통계청 | 한국표준질병사인분류. ICD-11 기반 | ★★★ 보건의료 적용 |
| **KDC** | 한국도서관협회 | 한국십진분류법. 10개 주류. 도서관 분류 | ★☆☆ 참조용 |
| **공통표준용어** | 행정안전부 | 9,027개 표준용어(2024.11). 공공기관 DB 표준 | ★★☆ 용어 참조 |

### 1.3 도메인별 전문 표준

| 표준명 | 도메인 | 특징 |
|--------|--------|------|
| **MeSH** | 의료 | Medical Subject Headings. 30,000+ 용어. NLM 관리 |
| **FIBO** | 금융 | Financial Industry Business Ontology. OWL 기반. OMG 표준 |
| **ICD-11** | 질병 | WHO 국제질병분류 11차. 2022년 발효 |
| **국가법령정보** | 법률 | 법제처 관리. 법령/판례/행정규칙 체계 |

### 1.4 공공데이터 분류체계

**data.go.kr 16개 분야:**
1. 공공행정
2. 과학기술
3. 교육
4. 교통물류
5. 국토관리
6. 농축수산
7. 문화관광
8. 법률
9. 보건의료
10. 사회복지
11. 산업고용
12. 식품건강
13. 재난안전
14. 재정금융
15. 통일외교안보
16. 환경기상

---

## 2. 현행 체계 분석

### 2.1 현재 구조 (v2.1)

```
10개 도메인 / 175개 분류 / 124개 용어
├── 01 공공행정 (16분류, 12용어)
├── 02 교육 (16분류, 5용어)
├── 03 보건의료 (22분류, 16용어)
├── 04 사회복지 (16분류, 9용어)
├── 05 법률 (15분류, 7용어)
├── 06 재정금융 (24분류, 16용어)
├── 07 산업경제 (20분류, 8용어)
├── 08 재난안전 (12분류, 3용어)
├── 09 문화관광 (17분류, 6용어)
└── 10 환경기상 (17분류, 4용어)
```

### 2.2 현행 체계의 문제점

1. **표준 연계 부족**: 국제/국내 표준과의 명시적 매핑 없음
2. **용어 불균형**: 도메인별 용어 수 편차 큼 (16 vs 3)
3. **동의어 불균형**: 공공행정/교육 도메인에 동의어 전무
4. **README 미정의**: 소분류의 설명이 간략함
5. **SKOS 미적용**: 시맨틱웹 표준 미반영

---

## 3. 재구축 설계 원칙

### 3.1 핵심 원칙

| 원칙 | 설명 |
|------|------|
| **표준 우선** | 국제/국내 표준 분류체계 우선 적용 |
| **계층 일관성** | 모든 도메인에서 동일한 계층 구조 유지 |
| **상호운용성** | SKOS/ISO 25964 호환성 확보 |
| **확장 가능성** | 신규 도메인/분류 추가 용이 |
| **다국어 지원** | 영문명/약어 필수 관리 |

### 3.2 적용할 표준

```
┌─────────────────────────────────────────────────────────────┐
│                    온톨로지 체계 구조                        │
├─────────────────────────────────────────────────────────────┤
│  메타 모델: SKOS + ISO 25964                                │
│  ├── skos:Concept (분류/용어)                               │
│  ├── skos:broader/narrower (계층 관계)                      │
│  ├── skos:related (연관 관계)                               │
│  ├── skos:prefLabel (대표 명칭)                             │
│  ├── skos:altLabel (동의어/이형어)                          │
│  └── skos:definition (정의)                                 │
├─────────────────────────────────────────────────────────────┤
│  도메인 분류: BRM + data.go.kr + 자체 확장                   │
├─────────────────────────────────────────────────────────────┤
│  도메인별 전문 표준:                                         │
│  ├── 보건의료: KCD (ICD-11), MeSH                           │
│  ├── 재정금융: FIBO, 금융감독원 분류                         │
│  ├── 공공행정: BRM (정부기능분류)                            │
│  ├── 산업경제: KSIC (한국표준산업분류)                       │
│  └── 법률: 법제처 국가법령 분류                              │
├─────────────────────────────────────────────────────────────┤
│  메타데이터: Dublin Core 요소 적용                           │
│  ├── dc:title, dc:description, dc:subject                   │
│  ├── dc:creator, dc:date, dc:language                       │
│  └── dc:identifier, dc:source, dc:relation                  │
└─────────────────────────────────────────────────────────────┘
```

---

## 4. 신규 분류체계 설계

### 4.1 도메인 구조 (3-Tier)

```
Tier 1: 대분류 (Domain) - 주제 영역
Tier 2: 중분류 (Category) - 세부 영역
Tier 3: 소분류 (Sub-category) - 구체 항목
```

### 4.2 도메인 재설계안

#### Option A: 확장형 (17개 도메인)

data.go.kr 16개 + 민간 도메인 추가

| 코드 | 도메인 | 영문 | 표준 참조 | 비고 |
|------|--------|------|-----------|------|
| 01 | 공공행정 | Public Administration | BRM | data.go.kr |
| 02 | 과학기술 | Science & Technology | OECD FOS | data.go.kr |
| 03 | 교육 | Education | UNESCO | data.go.kr |
| 04 | 교통물류 | Transportation & Logistics | KSIC | data.go.kr |
| 05 | 국토관리 | Land Management | - | data.go.kr |
| 06 | 농축수산 | Agriculture & Fisheries | KSIC | data.go.kr |
| 07 | 문화관광 | Culture & Tourism | UNESCO | data.go.kr |
| 08 | 법률 | Law & Legislation | 법제처 | data.go.kr |
| 09 | 보건의료 | Healthcare | KCD, MeSH | data.go.kr |
| 10 | 사회복지 | Social Welfare | - | data.go.kr |
| 11 | 산업고용 | Industry & Employment | KSIC | data.go.kr |
| 12 | 식품건강 | Food & Health | - | data.go.kr |
| 13 | 재난안전 | Disaster & Safety | - | data.go.kr |
| 14 | 재정금융 | Finance & Economy | FIBO | data.go.kr |
| 15 | 통일외교안보 | Diplomacy & Security | - | data.go.kr |
| 16 | 환경기상 | Environment & Weather | - | data.go.kr |
| 17 | 디지털커머스 | Digital Commerce | KSIC, 자체 | 확장 |

#### Option B: 핵심형 (12개 도메인) - **권장**

현재 문서 보유 + 핵심 공공 분야 중심

| 코드 | 도메인 | 영문 | 표준 참조 | 문서 디렉토리 |
|------|--------|------|-----------|--------------|
| 01 | 공공행정 | Public Administration | BRM | public/ |
| 02 | 교육 | Education | UNESCO | - |
| 03 | 보건의료 | Healthcare | KCD, MeSH | medical/ |
| 04 | 사회복지 | Social Welfare | - | - |
| 05 | 법률 | Law & Legislation | 법제처 | law/ |
| 06 | 재정금융 | Finance & Economy | FIBO | finance/ |
| 07 | 산업경제 | Industry & Economy | KSIC | - |
| 08 | 디지털커머스 | Digital Commerce | KSIC | commerce/ |
| 09 | 과학기술 | Science & Technology | OECD FOS | - |
| 10 | 재난안전 | Disaster & Safety | - | - |
| 11 | 문화관광 | Culture & Tourism | UNESCO | - |
| 12 | 환경기상 | Environment & Weather | - | - |

### 4.3 ID 체계 개선

#### 현행
```
분류: C + DD + LL + SSSS (9자리)
용어: T + DD + LL + SSSS (9자리)
```

#### 개선안
```
분류: C + DD + LLL + SSSS (10자리)
       │   │    │     └── 일련번호 (4자리)
       │   │    └── 중분류 코드 (3자리, 최대 999개)
       │   └── 도메인 코드 (2자리, 최대 99개)
       └── 타입 (C: Classification)

용어: T + DD + LLL + SSSS (10자리)
       └── 타입 (T: Term)

동의어: S + DD + LLL + SSSS (10자리)
        └── 타입 (S: Synonym)

관계: R + NNNNNNNN (9자리)
      └── 타입 (R: Relation)
```

### 4.4 표준 레퍼런스 데이터 모델

분류/용어 데이터에 국제/국내 표준에 대한 명시적 레퍼런스를 포함합니다.

#### 4.4.1 표준(Standard) 스키마

```yaml
# 표준(Standard) 정의 - 참조할 수 있는 국제/국내 표준 목록
Standard:
  id: string              # 표준 고유 ID (예: STD-SKOS, STD-BRM)
  code: string            # 표준 코드 (예: ISO-25964, KS-X-ISO-25964)
  name:
    ko: string            # 한글명
    en: string            # 영문명
  type: enum              # INTERNATIONAL | NATIONAL | DOMAIN
  scope: enum             # ONTOLOGY | CLASSIFICATION | TERMINOLOGY | METADATA
  organization: string    # 관리 기관 (예: W3C, ISO, 통계청)
  version: string         # 버전 (예: 2.0, 11차)
  published_date: date    # 발행일
  uri: string             # 공식 URI/URL
  description: string     # 표준 설명
  domains: []             # 적용 도메인 목록

# 표준 유형
StandardType:
  - INTERNATIONAL         # 국제 표준 (ISO, W3C, OECD 등)
  - NATIONAL              # 국내 표준 (KS, 통계청, 행안부 등)
  - DOMAIN                # 도메인 전문 표준 (MeSH, FIBO 등)

# 표준 범위
StandardScope:
  - ONTOLOGY              # 온톨로지 구조 (SKOS, OWL)
  - CLASSIFICATION        # 분류체계 (BRM, KSIC, KDC)
  - TERMINOLOGY           # 용어체계 (MeSH, ICD, FIBO)
  - METADATA              # 메타데이터 (Dublin Core)
```

#### 4.4.2 표준 레퍼런스(StandardReference) 스키마

```yaml
# 표준 레퍼런스 - 분류/용어와 표준 간의 매핑
StandardReference:
  standard_id: string     # 참조 표준 ID
  external_id: string     # 해당 표준 내 ID/코드
  external_name: string   # 해당 표준 내 명칭
  match_type: enum        # 매핑 유형
  confidence: float       # 매핑 신뢰도 (0.0 ~ 1.0)
  note: string            # 매핑 비고

# 매핑 유형 (SKOS 매핑 속성 기반)
MatchType:
  - EXACT_MATCH           # skos:exactMatch - 완전 일치
  - CLOSE_MATCH           # skos:closeMatch - 유사 일치
  - BROAD_MATCH           # skos:broadMatch - 상위 개념 일치
  - NARROW_MATCH          # skos:narrowMatch - 하위 개념 일치
  - RELATED_MATCH         # skos:relatedMatch - 연관 일치
  - DERIVED_FROM          # 해당 표준에서 파생됨
```

#### 4.4.3 SKOS 호환 분류(Classification) 스키마

```yaml
# 분류(Classification) 스키마 - 표준 레퍼런스 포함
Classification:
  # 기본 속성
  id: string              # C + DD + LLL + SSSS
  uri: string             # https://ontology.example.com/classification/{id}

  # SKOS 라벨
  prefLabel:              # skos:prefLabel
    ko: string
    en: string
  altLabel: []            # skos:altLabel (이형어)
  hiddenLabel: []         # skos:hiddenLabel (검색용 숨김 라벨)

  # SKOS 문서
  definition: string      # skos:definition
  scopeNote: string       # skos:scopeNote (범위 주석)
  example: string         # skos:example
  historyNote: string     # skos:historyNote (이력)

  # SKOS 관계
  broader: string         # 상위 분류 ID
  narrower: []            # 하위 분류 ID 목록
  related: []             # 연관 분류 ID 목록

  # SKOS 개념 체계
  notation: string        # skos:notation (분류 기호)
  inScheme: string        # 소속 ConceptScheme
  topConceptOf: string    # 최상위 개념 여부

  # ★ 표준 레퍼런스 (신규)
  standardRefs: []        # StandardReference 목록
  primaryStandard: string # 주요 참조 표준 ID

  # Dublin Core 메타데이터
  dcterms:
    created: date
    modified: date
    creator: string
    source: string        # 원천 출처
    license: string       # 라이선스
```

#### 4.4.4 SKOS 호환 용어(Term) 스키마

```yaml
# 용어(Term) 스키마 - 표준 레퍼런스 포함
Term:
  # 기본 속성
  id: string              # T + DD + LLL + SSSS
  uri: string

  # SKOS 라벨
  prefLabel:
    ko: string
    en: string
  altLabel: []            # 동의어
  acronym: string         # 약어

  # SKOS 문서
  definition: string
  scopeNote: string
  example: string

  # SKOS 관계
  broader: string         # 상위 용어 ID
  narrower: []
  related: []             # 연관 용어

  # 분류 연결
  belongsTo: string       # 소속 분류 ID

  # ★ 표준 레퍼런스 (신규)
  standardRefs: []        # StandardReference 목록
  primaryStandard: string # 주요 참조 표준 ID

  # Dublin Core 메타데이터
  dcterms:
    created: date
    modified: date
    source: string
```

#### 4.4.5 표준 레지스트리 예시

```yaml
# standards_registry.yaml - 참조 표준 목록
standards:
  # === 국제 표준 (INTERNATIONAL) ===

  - id: STD-SKOS
    code: W3C-SKOS
    name:
      ko: 단순지식조직체계
      en: Simple Knowledge Organization System
    type: INTERNATIONAL
    scope: ONTOLOGY
    organization: W3C
    version: "1.0"
    published_date: 2009-08-18
    uri: https://www.w3.org/TR/skos-reference/
    description: 시소러스, 분류체계, 택소노미 등을 표현하기 위한 W3C 표준

  - id: STD-ISO25964
    code: ISO-25964
    name:
      ko: 시소러스 및 다른 어휘와의 상호운용성
      en: Thesauri and interoperability with other vocabularies
    type: INTERNATIONAL
    scope: ONTOLOGY
    organization: ISO
    version: "2013"
    published_date: 2013-03-01
    uri: https://www.iso.org/standard/53658.html
    description: 시소러스 구축 및 상호운용성을 위한 국제 표준

  - id: STD-DC
    code: ISO-15836
    name:
      ko: 더블린 코어 메타데이터
      en: Dublin Core Metadata Element Set
    type: INTERNATIONAL
    scope: METADATA
    organization: DCMI
    version: "1.1"
    uri: https://www.dublincore.org/specifications/dublin-core/dces/
    description: 15개 핵심 메타데이터 요소 표준

  - id: STD-UNESCO
    code: UNESCO-THES
    name:
      ko: 유네스코 시소러스
      en: UNESCO Thesaurus
    type: INTERNATIONAL
    scope: TERMINOLOGY
    organization: UNESCO
    version: "2024"
    uri: https://vocabularies.unesco.org/browser/thesaurus/en/
    description: 교육, 문화, 과학 분야 다국어 시소러스
    domains: [02, 09, 11]  # 교육, 과학기술, 문화관광

  - id: STD-OECD-FOS
    code: OECD-FOS
    name:
      ko: OECD 과학기술분류
      en: OECD Fields of Science and Technology
    type: INTERNATIONAL
    scope: CLASSIFICATION
    organization: OECD
    version: "2007"
    uri: https://www.oecd.org/science/inno/38235147.pdf
    description: 6개 대분류, 42개 소분류의 과학기술 분야 분류체계
    domains: [09]  # 과학기술

  - id: STD-FIBO
    code: OMG-FIBO
    name:
      ko: 금융산업비즈니스온톨로지
      en: Financial Industry Business Ontology
    type: INTERNATIONAL
    scope: TERMINOLOGY
    organization: EDM Council / OMG
    version: "2024Q3"
    uri: https://spec.edmcouncil.org/fibo/
    description: 금융 산업을 위한 OWL 기반 온톨로지
    domains: [06]  # 재정금융

  - id: STD-MESH
    code: NLM-MESH
    name:
      ko: 의학주제표목
      en: Medical Subject Headings
    type: INTERNATIONAL
    scope: TERMINOLOGY
    organization: NLM (미국 국립의학도서관)
    version: "2025"
    uri: https://www.nlm.nih.gov/mesh/
    description: 생의학 및 건강 관련 정보 색인용 통제 어휘
    domains: [03]  # 보건의료

  - id: STD-ICD11
    code: WHO-ICD-11
    name:
      ko: 국제질병분류 11차
      en: International Classification of Diseases 11th Revision
    type: INTERNATIONAL
    scope: CLASSIFICATION
    organization: WHO
    version: "11"
    published_date: 2022-01-01
    uri: https://icd.who.int/
    description: 세계보건기구 국제질병분류 체계
    domains: [03]  # 보건의료

  # === 국내 표준 (NATIONAL) ===

  - id: STD-BRM
    code: MOIS-BRM
    name:
      ko: 정부기능분류체계
      en: Business Reference Model
    type: NATIONAL
    scope: CLASSIFICATION
    organization: 행정안전부
    version: "2024"
    uri: https://www.data.go.kr/data/15062615/fileData.do
    description: 정부 업무를 기능 중심으로 분류하는 6레벨 체계
    domains: [01]  # 공공행정

  - id: STD-KSIC
    code: KOSTAT-KSIC
    name:
      ko: 한국표준산업분류
      en: Korean Standard Industrial Classification
    type: NATIONAL
    scope: CLASSIFICATION
    organization: 통계청
    version: "11차 (2024)"
    published_date: 2024-07-01
    uri: http://kssc.kostat.go.kr/
    description: 산업 활동을 유형화한 5레벨 표준 분류체계
    domains: [07, 08]  # 산업경제, 디지털커머스

  - id: STD-KCD
    code: KOSTAT-KCD
    name:
      ko: 한국표준질병사인분류
      en: Korean Standard Classification of Diseases
    type: NATIONAL
    scope: CLASSIFICATION
    organization: 통계청
    version: "8차"
    uri: https://www.kcdcode.kr/
    description: ICD 기반 한국 실정에 맞는 질병 분류체계
    domains: [03]  # 보건의료

  - id: STD-MOLEG
    code: MOLEG-LAW
    name:
      ko: 국가법령분류체계
      en: National Law Classification System
    type: NATIONAL
    scope: CLASSIFICATION
    organization: 법제처
    uri: https://www.law.go.kr/
    description: 법령, 판례, 행정규칙 분류 체계
    domains: [05]  # 법률

  - id: STD-DATAGOkr
    code: MOIS-OPENDATA
    name:
      ko: 공공데이터 분류체계
      en: Public Data Classification
    type: NATIONAL
    scope: CLASSIFICATION
    organization: 행정안전부
    version: "2024"
    uri: https://www.data.go.kr/
    description: 공공데이터포털 16개 분야 분류체계

  - id: STD-STDTERM
    code: MOIS-STDTERM
    name:
      ko: 공공데이터 공통표준용어
      en: Public Data Standard Terminology
    type: NATIONAL
    scope: TERMINOLOGY
    organization: 행정안전부
    version: "7차 (2024.11)"
    uri: https://www.data.go.kr/
    description: 공공기관 DB 표준화를 위한 9,027개 표준용어

  # === 한국형 응용 표준 (KOREAN APPLICATION PROFILES) ===

  - id: STD-DCAT-AP-KR
    code: DCAT-AP-KR
    name:
      ko: 대한민국 데이터 카탈로그 응용 프로파일
      en: DCAT Application Profile for Korea
    type: NATIONAL
    scope: METADATA
    organization: 한국데이터산업진흥원
    version: "1.0 (DCAT-AP 2.1.0 기반)"
    uri: https://vocab.datahub.kr/spec/dcat-ap-kr/
    description: 데이터 포털용 메타데이터 명세. DCAT-AP를 한국 환경에 맞게 확장
    note: |
      - 네임스페이스: dcatkr (http://vocab.datahub.kr/def/dcat-ap-kr/)
      - 핵심 클래스: Catalog, Dataset, Distribution, DataService
      - 한국 특화 속성: maintainer, numberOfView, numberOfDownload, legalBasis, fee

  - id: STD-KOOR
    code: KOOR
    name:
      ko: 한국 기관 표현 어휘
      en: Korean Organization Vocabulary
    type: NATIONAL
    scope: TERMINOLOGY
    organization: 한국데이터산업진흥원
    uri: http://vocab.datahub.kr/def/organization/
    description: 공공/민간 기관을 표현하기 위한 RDF 어휘
    note: |
      - 기관 유형: 행정기관, 헌법기관, 교육기관, 사법기관, 입법기관, 국군조직, 민간/공공기관

  - id: STD-ADMCODE
    code: MOIS-ADMCODE
    name:
      ko: 행정표준코드
      en: Administrative Standard Code
    type: NATIONAL
    scope: CLASSIFICATION
    organization: 행정안전부
    uri: https://www.code.go.kr/
    description: 행정업무에 필요한 표준화된 행정코드 체계
    note: |
      - 법정동코드 (10자리): 시도(2) + 시군구(3) + 읍면동(3) + 리(2)
      - 행정동코드 (10자리): 행정기관 관할 구역
      - 기관코드, 직종코드, 직위코드 등 포함

  - id: STD-KS-ISO11179
    code: KS-X-ISO11179
    name:
      ko: 메타데이터 레지스트리
      en: Metadata Registry (MDR)
    type: NATIONAL
    scope: METADATA
    organization: 국가기술표준원
    version: "KS X ISO/IEC 11179 시리즈"
    uri: https://www.kssn.net/
    description: ISO 11179 기반 메타데이터 레지스트리 한국산업표준
    note: |
      - Part 1: 프레임워크
      - Part 3: 레지스트리 메타모델과 기본 속성
      - Part 4: 데이터 정의의 정형화
      - Part 5: 명명 원칙
      - Part 6: 등록

  - id: STD-DBSTD
    code: MOIS-DBSTD
    name:
      ko: 공공기관 데이터베이스 표준화 지침
      en: Public Institution Database Standardization Guidelines
    type: NATIONAL
    scope: METADATA
    organization: 행정안전부
    version: "2023-18호 (2023.4.3)"
    uri: https://www.law.go.kr/행정규칙/공공기관의데이터베이스표준화지침/
    description: 공공기관 DB 구축 시 준수해야 할 표준화 지침
    note: |
      - 메타데이터 표준 관리항목: 38개
      - 공통표준용어 적용 의무화
      - 데이터 품질관리 기준 포함

  - id: STD-DATAQUALITY
    code: MOIS-DQ
    name:
      ko: 공공데이터 품질관리 수준평가
      en: Public Data Quality Management Assessment
    type: NATIONAL
    scope: METADATA
    organization: 행정안전부
    version: "2024"
    uri: https://www.data.go.kr/ugs/selectPublicDataQlityView.do
    description: 공공기관 데이터 품질관리 수준 진단 및 평가 체계
    note: |
      - 평가 영역: 계획, 구축, 운영, 활용
      - 평가 대상: 679개 기관 (2024년 기준)
      - 2016년부터 시행
```

#### 4.4.6 표준 레퍼런스 적용 예시

```yaml
# 분류 예시: 공공행정 > 정부조직·기관관리
classification_example:
  id: C0101001
  uri: https://ontology.example.com/classification/C0101001
  prefLabel:
    ko: 정부조직·기관관리
    en: Government Organization Management
  definition: 정부조직 및 공공기관의 구조, 인력, 운영에 관한 분류
  broader: C0100001
  notation: "01.01"

  # ★ 표준 레퍼런스
  standardRefs:
    - standard_id: STD-BRM
      external_id: "010101"
      external_name: 정부기능관리
      match_type: CLOSE_MATCH
      confidence: 0.9
      note: BRM 정책영역 '일반공공행정' 하위 매핑

    - standard_id: STD-DATAGOkr
      external_id: "01"
      external_name: 공공행정
      match_type: BROAD_MATCH
      confidence: 1.0

  primaryStandard: STD-BRM

# 용어 예시: 암
term_example:
  id: T0301001
  uri: https://ontology.example.com/term/T0301001
  prefLabel:
    ko: 암
    en: Cancer
  altLabel: [악성종양, 악성신생물, Malignant Neoplasm]
  definition: 비정상적인 세포의 무제한적 성장과 전이를 특징으로 하는 질환
  belongsTo: C0305001  # 질병관리

  # ★ 표준 레퍼런스
  standardRefs:
    - standard_id: STD-MESH
      external_id: D009369
      external_name: Neoplasms
      match_type: EXACT_MATCH
      confidence: 1.0
      note: MeSH descriptor ID

    - standard_id: STD-ICD11
      external_id: "2"
      external_name: Neoplasms
      match_type: BROAD_MATCH
      confidence: 0.95
      note: ICD-11 Chapter 2

    - standard_id: STD-KCD
      external_id: "C00-D48"
      external_name: 신생물
      match_type: BROAD_MATCH
      confidence: 0.95

  primaryStandard: STD-MESH

# 용어 예시: 핀테크
term_example_fintech:
  id: T0604001
  uri: https://ontology.example.com/term/T0604001
  prefLabel:
    ko: 핀테크
    en: FinTech
  acronym: FinTech
  altLabel: [금융기술, Financial Technology]
  definition: 금융(Finance)과 기술(Technology)의 합성어로, 정보기술을 활용한 혁신적 금융서비스
  belongsTo: C0604001  # 핀테크·혁신금융

  # ★ 표준 레퍼런스
  standardRefs:
    - standard_id: STD-FIBO
      external_id: fibo-fbc-fct-fse/FinancialTechnologyCompany
      external_name: Financial Technology Company
      match_type: RELATED_MATCH
      confidence: 0.8
      note: FIBO Financial Business and Commerce 모듈

    - standard_id: STD-KSIC
      external_id: "64"
      external_name: 금융업
      match_type: BROAD_MATCH
      confidence: 0.7

  primaryStandard: STD-FIBO
```

---

## 5. 도메인별 표준 매핑 계획

### 5.1 공공행정 (01)

**참조 표준:** BRM (정부기능분류체계)

```
BRM 6레벨 → 온톨로지 3레벨 매핑

BRM 정책분야 (17개)      → 도메인 (01 공공행정)
BRM 정책영역 (76개)      → 중분류
BRM 대기능/중기능        → 소분류
BRM 소기능/단위과제      → (용어 참조)
```

| BRM 정책분야 | 온톨로지 중분류 |
|-------------|----------------|
| 일반공공행정 | 정부조직·기관관리 |
| 공공질서및안전 | 행정정보화 |
| 통일·외교 | 국가정책·사업 |
| 국방 | - |
| 교육 | → 02 교육 도메인 |
| 문화및관광 | → 11 문화관광 도메인 |

### 5.2 보건의료 (03)

**참조 표준:** KCD (ICD-11), MeSH

```
KCD 구조 → 온톨로지 매핑

KCD 대분류 (22장)        → 중분류 참조
MeSH 카테고리 (16개)     → 용어 체계 참조
```

| MeSH 카테고리 | 온톨로지 중분류 |
|---------------|----------------|
| Anatomy | - |
| Organisms | - |
| Diseases | 질병관리 |
| Chemicals and Drugs | - |
| Analytical, Diagnostic and Therapeutic Techniques | 의료이용 |
| Health Care | 의료기관, 건강보험 |

### 5.3 재정금융 (06)

**참조 표준:** FIBO (Financial Industry Business Ontology)

#### 5.3.1 FIBO 개요

FIBO는 금융 산업을 위한 OWL 기반 온톨로지로, EDM Council에서 관리하고 OMG에서 표준화했습니다.
- **버전:** 2025Q3 Production
- **규모:** 2,457개 클래스, 10개 도메인
- **라이선스:** MIT (오픈소스)
- **공식 URI:** https://spec.edmcouncil.org/fibo/

#### 5.3.2 FIBO 도메인 구조 (10개)

```
FIBO
├── FND (Foundations)           # 기초 개념
│   ├── Accounting              # 회계
│   ├── Agreements              # 계약/협정
│   ├── Arrangements            # 배열/구성
│   ├── Organizations           # 조직
│   ├── Places                  # 장소
│   ├── Relations               # 관계
│   └── Utilities               # 유틸리티
│
├── BE (Business Entities)      # 사업체
│   ├── Corporations            # 법인
│   ├── FunctionalEntities      # 기능적 실체
│   ├── GovernmentEntities      # 정부 기관
│   ├── LegalEntities           # 법적 실체
│   ├── OwnershipAndControl     # 소유/지배
│   └── Partnerships            # 파트너십
│
├── FBC (Financial Business & Commerce)  # 금융비즈니스
│   ├── DebtAndEquities         # 부채/자본
│   ├── FunctionalEntities      # 금융기관
│   ├── FinancialInstruments    # 금융상품
│   ├── ProductsAndServices     # 제품/서비스
│   └── RegistrationAuthorities # 등록기관
│
├── SEC (Securities)            # 증권
│   ├── Securities              # 증권 공통
│   │   ├── Identification      # 식별
│   │   ├── Classification      # 분류 (CFI)
│   │   ├── Issuance            # 발행
│   │   └── Listings            # 상장
│   ├── Equities                # 주식
│   │   ├── EquityInstruments   # 주식상품
│   │   └── DepositaryReceipts  # 예탁증권 (DR)
│   ├── Debt                    # 채권
│   │   ├── Bonds               # 채권
│   │   ├── AssetBackedSecurities # ABS
│   │   └── ShortTermDebt       # 단기채
│   └── Funds                   # 펀드
│       ├── CollectiveInvestmentVehicles  # CIV
│       ├── ETFs                # ETF
│       ├── MutualFunds         # 뮤추얼펀드
│       └── HedgeFunds          # 헤지펀드
│
├── DER (Derivatives)           # 파생상품
│   ├── DerivativesContracts    # 파생계약
│   ├── Options                 # 옵션
│   ├── Futures                 # 선물
│   ├── Forwards                # 선도
│   ├── Swaps                   # 스왑
│   └── CreditDerivatives       # 신용파생
│
├── LOAN (Loans)                # 대출
│   ├── LoanContracts           # 대출계약
│   ├── CommercialLoans         # 기업대출
│   ├── ConsumerLoans           # 소비자대출
│   ├── MortgageLoans           # 주택담보대출
│   ├── AutoLoans               # 자동차대출
│   └── StudentLoans            # 학자금대출
│
├── IND (Indices & Indicators)  # 지수/지표
│   ├── EconomicIndicators      # 경제지표
│   ├── InterestRates           # 금리
│   ├── ForeignExchange         # 외환
│   └── MarketIndices           # 시장지수
│
├── CAE (Corporate Actions)     # 기업활동
│   └── CorporateEvents         # 기업이벤트
│
├── BP (Business Process)       # 비즈니스 프로세스
│   ├── SecuritiesIssuance      # 증권발행
│   └── TransactionWorkflows    # 거래워크플로우
│
└── MD (Market Data)            # 시장데이터
    ├── Prices                  # 가격
    ├── Yields                  # 수익률
    └── Analytics               # 분석
```

#### 5.3.3 FIBO → 온톨로지 매핑

| FIBO 도메인 | FIBO 모듈 | 온톨로지 중분류 | 매핑 용어 예시 |
|-------------|-----------|-----------------|---------------|
| **FND** | Agreements | 금융정책 | 계약, 협정 |
| **FND** | Organizations | 금융기관 | 조직, 기관 |
| **BE** | Corporations | 금융기관 | 법인, 기업 |
| **BE** | GovernmentEntities | 금융정책 | 규제기관, 중앙은행 |
| **FBC** | FunctionalEntities | 금융기관 | 은행, 보험사, 증권사 |
| **FBC** | FinancialInstruments | 금융상품 | 금융상품 일반 |
| **SEC** | Equities | 자본시장 | 주식, 보통주, 우선주 |
| **SEC** | Debt | 자본시장 | 채권, 회사채, 국채 |
| **SEC** | Funds | 자본시장 | 펀드, ETF, 뮤추얼펀드 |
| **DER** | Options/Futures | 파생상품 | 옵션, 선물, 스왑 |
| **LOAN** | MortgageLoans | 여신/대출 | 주택담보대출 |
| **LOAN** | ConsumerLoans | 여신/대출 | 가계대출, 소비자금융 |
| **IND** | InterestRates | 금융지표 | 기준금리, SOFR, KOFR |
| **IND** | EconomicIndicators | 경제지표 | GDP, 물가지수, 실업률 |
| **IND** | ForeignExchange | 외환 | 환율, 통화 |
| **MD** | Prices | 시장데이터 | 시세, 호가, 체결가 |

#### 5.3.4 재정금융 도메인 중분류 재설계 (FIBO 기반)

```
06 재정금융 (Finance & Economy)
├── C0601 통화정책 (Monetary Policy)
│   ├── 기준금리 운영
│   ├── 공개시장운영
│   └── 유동성조절
│   → FIBO: FND/Agreements, IND/InterestRates
│
├── C0602 금융안정 (Financial Stability)
│   ├── 가계부채 관리
│   ├── 부동산PF 리스크
│   └── 시스템리스크
│   → FIBO: FBC/DebtAndEquities, LOAN
│
├── C0603 금융기관 (Financial Institutions)
│   ├── 은행
│   ├── 보험사
│   ├── 증권사
│   └── 기타 금융회사
│   → FIBO: BE/Corporations, FBC/FunctionalEntities
│
├── C0604 자본시장 (Capital Markets)
│   ├── 주식시장
│   ├── 채권시장
│   ├── 펀드
│   └── 파생상품
│   → FIBO: SEC (Equities, Debt, Funds), DER
│
├── C0605 여신/대출 (Lending)
│   ├── 기업대출
│   ├── 가계대출
│   ├── 주택담보대출
│   └── 소상공인금융
│   → FIBO: LOAN
│
├── C0606 금융지표 (Financial Indicators)
│   ├── 금리
│   ├── 환율
│   ├── 시장지수
│   └── 경제지표
│   → FIBO: IND
│
├── C0607 핀테크/혁신금융 (FinTech)
│   ├── 디지털금융
│   ├── 빅테크금융
│   └── 오픈뱅킹
│   → FIBO: FBC/ProductsAndServices (확장)
│
├── C0608 연금/보험 (Pension & Insurance)
│   ├── 공적연금
│   ├── 퇴직연금
│   └── 보험상품
│   → FIBO: BE, FBC/ProductsAndServices
│
└── C0609 국가재정 (Public Finance)
    ├── 국가예산
    ├── 조세/세금
    └── 지방재정
    → FIBO: BE/GovernmentEntities
```

#### 5.3.5 FIBO 용어 매핑 예시

```yaml
# 기준금리
- term_id: T0601001
  prefLabel:
    ko: 기준금리
    en: Base Rate
  standardRefs:
    - standard_id: STD-FIBO
      external_id: fibo-ind-ir-ir/BaseRate
      external_name: Base Rate
      match_type: EXACT_MATCH
      confidence: 1.0

# 주식
- term_id: T0604001
  prefLabel:
    ko: 주식
    en: Equity
  standardRefs:
    - standard_id: STD-FIBO
      external_id: fibo-sec-eq-eq/Equity
      external_name: Equity
      match_type: EXACT_MATCH
      confidence: 1.0

# 채권
- term_id: T0604002
  prefLabel:
    ko: 채권
    en: Bond
  standardRefs:
    - standard_id: STD-FIBO
      external_id: fibo-sec-dbt-bnd/Bond
      external_name: Bond
      match_type: EXACT_MATCH
      confidence: 1.0

# 파생상품
- term_id: T0604003
  prefLabel:
    ko: 파생상품
    en: Derivative
  standardRefs:
    - standard_id: STD-FIBO
      external_id: fibo-der-drc/DerivativeContract
      external_name: Derivative Contract
      match_type: EXACT_MATCH
      confidence: 1.0

# 주택담보대출
- term_id: T0605001
  prefLabel:
    ko: 주택담보대출
    en: Mortgage Loan
  standardRefs:
    - standard_id: STD-FIBO
      external_id: fibo-loan-ln-ln/MortgageLoan
      external_name: Mortgage Loan
      match_type: EXACT_MATCH
      confidence: 1.0

# ETF
- term_id: T0604004
  prefLabel:
    ko: 상장지수펀드
    en: Exchange-Traded Fund
  acronym: ETF
  standardRefs:
    - standard_id: STD-FIBO
      external_id: fibo-sec-fund-etf/ExchangeTradedFund
      external_name: Exchange Traded Fund
      match_type: EXACT_MATCH
      confidence: 1.0
```

### 5.4 산업경제 (07) / 디지털커머스 (08)

**참조 표준:** KSIC (한국표준산업분류)

```
KSIC 5레벨 → 온톨로지 매핑

KSIC 대분류 (21개)       → 도메인 참조
KSIC 중분류 (77개)       → 중분류
KSIC 소분류 (232개)      → 소분류
```

| KSIC 대분류 | 도메인 매핑 |
|-------------|------------|
| G. 도매 및 소매업 | 08 디지털커머스 |
| J. 정보통신업 | 08 디지털커머스 |
| K. 금융 및 보험업 | 06 재정금융 |
| M. 전문, 과학 및 기술 서비스업 | 09 과학기술 |
| Q. 보건업 및 사회복지 서비스업 | 03 보건의료, 04 사회복지 |

### 5.5 한국형 응용 표준 적용

#### 5.5.1 DCAT-AP-KR 적용

DCAT-AP-KR은 데이터 포털의 메타데이터 상호운용성을 위한 한국형 표준입니다.

**적용 범위:**
- 온톨로지 데이터를 데이터셋으로 공개할 때 DCAT-AP-KR 메타데이터 적용
- 분류/용어 데이터의 카탈로그화

**DCAT-AP-KR 클래스 매핑:**

```yaml
# 온톨로지 → DCAT-AP-KR 매핑
OntologyDataset:
  type: dcat:Dataset
  title: "MC 분류·용어 통합 체계"
  description: "공공/민간 도메인의 분류 및 용어 온톨로지"

  # DCAT-AP-KR 필수 속성
  dct:title: "MC 분류·용어 통합 체계"
  dct:description: "10개 도메인, 175개 분류, 124개 용어를 포함하는 온톨로지"

  # DCAT-AP-KR 권장 속성
  dcat:distribution:
    - format: JSON (context.json)
    - format: SQL (ontology.sql)
    - format: RDF/SKOS (context.rdf)
    - format: Cypher (context.cypher)
  dct:publisher: # koor:Organization
  dcat:theme: # 분류 주제
  dcatkr:maintainer: # 관리기관

  # DCAT-AP-KR 한국 특화 속성
  dcatkr:legalBasis: "공공데이터법 제23조"
  dcatkr:fee: false
  dcatkr:numberOfRow: 299  # 분류 175 + 용어 124
```

**배포(Distribution) 정의:**

```yaml
distributions:
  - id: dist-json
    dcat:accessURL: https://example.com/ontology/context.json
    dcat:downloadURL: https://example.com/ontology/context.json
    dct:format: application/json
    dcat:mediaType: application/json
    dcatkr:numberOfDownload: 0

  - id: dist-rdf
    dcat:accessURL: https://example.com/ontology/context.rdf
    dct:format: application/rdf+xml
    dct:conformsTo: STD-SKOS  # SKOS 표준 준수

  - id: dist-sql
    dcat:accessURL: https://example.com/ontology/ontology.sql
    dct:format: text/x-sql
```

#### 5.5.2 행정표준코드 연계

공공행정 도메인의 지역/기관 관련 분류에 행정표준코드 연계:

```yaml
# 행정구역 분류와 행정표준코드 연계
classification_example:
  id: C0102001
  prefLabel:
    ko: 지방행정·자치
    en: Local Administration

  standardRefs:
    - standard_id: STD-ADMCODE
      external_id: "법정동코드"
      match_type: RELATED_MATCH
      note: 하위 분류에서 법정동코드 체계 참조

    - standard_id: STD-BRM
      external_id: "010102"
      external_name: 지방행정
      match_type: CLOSE_MATCH

# 용어 예시: 행정구역
term_example:
  id: T0102001
  prefLabel:
    ko: 행정구역
    en: Administrative District

  standardRefs:
    - standard_id: STD-ADMCODE
      external_id: "법정동코드 체계"
      match_type: DERIVED_FROM
      note: |
        10자리 코드 체계: 시도(2) + 시군구(3) + 읍면동(3) + 리(2)
        예: 1100000000 (서울특별시)
```

#### 5.5.3 공공데이터 공통표준용어 연계

공통표준용어(9,027개)와 온톨로지 용어 간 매핑:

```yaml
# 공통표준용어 매핑 예시
term_mappings:
  - term_id: T0601001
    prefLabel:
      ko: 기준금리
    standardRefs:
      - standard_id: STD-STDTERM
        external_id: "기준금리"
        external_name: "기준금리"
        match_type: EXACT_MATCH
        note: 공통표준용어 7차 제정 (2024.11)

  - term_id: T0301001
    prefLabel:
      ko: 암
    standardRefs:
      - standard_id: STD-STDTERM
        external_id: "암종류코드"
        match_type: RELATED_MATCH
        note: 관련 공통표준용어 존재

  - term_id: T0102001
    prefLabel:
      ko: 행정구역
    standardRefs:
      - standard_id: STD-STDTERM
        external_id: "행정구역코드"
        match_type: EXACT_MATCH
```

#### 5.5.4 KS X ISO/IEC 11179 준수

메타데이터 레지스트리 표준 준수를 위한 설계:

```yaml
# ISO 11179 준수 데이터 요소 정의
DataElement:
  # Part 3: 레지스트리 메타모델
  identifier: string        # 고유 식별자
  name: string              # 명칭
  definition: string        # 정의

  # Part 4: 데이터 정의 정형화
  conceptual_domain: string # 개념 도메인
  value_domain: string      # 값 도메인

  # Part 5: 명명 원칙
  naming_convention: |
    - 분류: C + DD + LLL + SSSS
    - 용어: T + DD + LLL + SSSS
    - 표준 약어 사용 (ISO 3166 국가코드 등)

  # Part 6: 등록
  registration_status: enum  # 등록 상태
  registration_authority: string  # 등록 기관
  submission_date: date
  effective_date: date
```

#### 5.5.5 한국형 표준 적용 요약

| 표준 | 적용 영역 | 적용 방식 |
|------|----------|----------|
| **DCAT-AP-KR** | 전체 온톨로지 | 데이터셋 메타데이터로 공개 시 적용 |
| **KOOR** | 기관 정보 | publisher, maintainer 속성에 적용 |
| **행정표준코드** | 공공행정 도메인 | 지역/기관 분류에 코드 연계 |
| **공통표준용어** | 모든 용어 | 일치하는 표준용어와 매핑 |
| **KS X ISO 11179** | 데이터 모델 | 메타데이터 구조 설계 시 준수 |
| **DB표준화지침** | 출력 SQL | SQL 생성 시 명명규칙 준수 |
| **품질관리평가** | 품질 관리 | 데이터 품질 지표 적용 |

---

## 6. 구현 로드맵

### Phase 1: 기반 구축 (1단계)

**목표:** SKOS 호환 데이터 모델 구축

- [ ] 신규 ID 체계 적용 (10자리)
- [ ] SKOS 속성 추가 (uri, broader, narrower, related)
- [ ] Dublin Core 메타데이터 추가
- [ ] context.json 스키마 확장
- [ ] 생성 스크립트 업데이트

**산출물:**
- `context_schema_v2.md` - 신규 스키마 문서
- `context.json` v2.0 - 확장된 마스터 데이터
- `generate_skos.py` - SKOS RDF 생성기

### Phase 2: 표준 매핑 (2단계)

**목표:** 도메인별 표준 연계

- [ ] BRM → 공공행정 매핑
- [ ] KSIC → 산업경제/디지털커머스 매핑
- [ ] KCD/MeSH → 보건의료 매핑
- [ ] FIBO → 재정금융 매핑
- [ ] 법제처 분류 → 법률 매핑

**산출물:**
- `standard_mappings/` - 표준 매핑 정의 디렉토리
- `mapping_brm.json` - BRM 매핑
- `mapping_ksic.json` - KSIC 매핑

### Phase 3: 데이터 확충 (3단계)

**목표:** 용어/관계 확장

- [ ] 도메인별 용어 균형화 (최소 15개/도메인)
- [ ] 동의어 확충 (모든 도메인)
- [ ] 연관 관계 확장
- [ ] README/정의 상세화

**산출물:**
- 분류 200개+ / 용어 200개+ / 동의어 200개+

### Phase 4: 출력 확장 (4단계)

**목표:** 다양한 포맷 지원

- [ ] SKOS RDF/XML 출력
- [ ] SKOS Turtle 출력
- [ ] JSON-LD 출력
- [ ] SPARQL 엔드포인트 지원

**산출물:**
- `context.rdf` - SKOS RDF
- `context.ttl` - Turtle 포맷
- `context.jsonld` - JSON-LD

---

## 7. 파일 구조 변경안

### 현행
```
ontology/
├── context.txt           # 마스터 (텍스트)
├── context.json          # 마스터 (JSON)
├── enhanced_data.py      # 상세 데이터
├── ontology.sql          # SQL 출력
├── context.cypher        # Cypher 출력
└── *.py                  # 생성 스크립트
```

### 변경안
```
ontology/
├── source/                      # 원본 데이터
│   ├── context.json             # 마스터 데이터 v2.0
│   ├── enhanced_data.py         # 상세 정의
│   └── standard_mappings/       # 표준 매핑
│       ├── mapping_brm.json
│       ├── mapping_ksic.json
│       ├── mapping_kcd.json
│       └── mapping_fibo.json
│
├── generated/                   # 생성 파일
│   ├── sql/
│   │   ├── ontology.sql
│   │   ├── mc_clsf.sql
│   │   ├── mc_term.sql
│   │   └── mc_term_rel.sql
│   ├── graph/
│   │   └── context.cypher
│   ├── skos/
│   │   ├── context.rdf
│   │   ├── context.ttl
│   │   └── context.jsonld
│   └── text/
│       ├── context.txt
│       └── context_minimal.txt
│
├── scripts/                     # 생성 스크립트
│   ├── build_context.py
│   ├── generate_sql.py
│   ├── generate_cypher.py
│   ├── generate_skos.py
│   └── validate.py
│
├── docs/                        # 문서
│   ├── context_schema.md
│   ├── standard_mappings.md
│   └── README.md
│
└── CLAUDE.md                    # 작업 가이드
```

---

## 8. 검토 및 결정 사항

### 8.1 확정 필요 사항

| 항목 | 옵션 | 권장 |
|------|------|------|
| 도메인 수 | 12개 / 17개 | **12개** (핵심형) |
| ID 체계 | 9자리 / 10자리 | **10자리** (확장) |
| SKOS 출력 | RDF만 / RDF+Turtle+JSON-LD | **전체** |
| 표준 매핑 | 필수 5개 | BRM, KSIC, KCD, FIBO, 법제처 |

### 8.2 우선순위

1. **High**: SKOS 호환 데이터 모델, ID 체계 변경
2. **Medium**: 표준 매핑, 용어 확충
3. **Low**: 신규 출력 포맷, 디렉토리 구조 변경

---

## 9. 참고 자료

### 국제 표준
- [SKOS Reference](https://www.w3.org/TR/skos-reference/) - W3C
- [ISO 25964](https://www.niso.org/schemas/iso25964) - NISO
- [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) - DCMI
- [Schema.org](https://schema.org/docs/schemas.html)
- [UNESCO Thesaurus](https://vocabularies.unesco.org/browser/thesaurus/en/)
- [FIBO](https://spec.edmcouncil.org/fibo/) - EDM Council

### 국내 표준
- [BRM 정부기능분류](https://www.data.go.kr/data/15062615/fileData.do) - 행정안전부
- [KSIC 한국표준산업분류](http://kssc.kostat.go.kr/) - 통계청
- [KCD 질병분류](https://www.kcdcode.kr/) - 통계청
- [공공데이터 공통표준용어](https://www.data.go.kr/) - 행정안전부

### 도메인별 표준
- [MeSH](https://www.nlm.nih.gov/mesh/meshhome.html) - NLM
- [국가법령정보센터](https://www.law.go.kr/) - 법제처

---

**문서 종료**
