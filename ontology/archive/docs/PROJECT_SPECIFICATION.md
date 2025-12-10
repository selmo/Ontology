# MC 분류·용어 통합 체계 프로젝트 명세서

**프로젝트명:** MC Classification and Terminology Integration System
**버전:** 2.1.0
**최종 업데이트:** 2025-12-02
**기준:** 공공데이터포털(data.go.kr) 실제 데이터셋 분석
**라이선스:** Based on data.go.kr classification system

---

## 목차

1. [프로젝트 개요](#1-프로젝트-개요)
2. [시스템 아키텍처](#2-시스템-아키텍처)
3. [데이터 모델](#3-데이터-모델)
4. [파일 구조](#4-파일-구조)
5. [데이터 흐름](#5-데이터-흐름)
6. [API 및 인터페이스](#6-api-및-인터페이스)
7. [출력 형식](#7-출력-형식)
8. [품질 관리](#8-품질-관리)
9. [버전 이력](#9-버전-이력)
10. [향후 계획](#10-향후-계획)

---

## 1. 프로젝트 개요

### 1.1 목적

문서 분류 및 용어 관리를 위한 체계적인 온톨로지 시스템 구축. 공공데이터포털(data.go.kr)의 16개 표준 분류체계 중 10개를 선별하여 실제 공개 데이터셋 200+ 개를 분석하여 구축.

### 1.2 핵심 기능

- **분류 체계 관리**: 계층적 분류 구조 (175개 분류)
- **용어 관리**: 도메인별 핵심 용어 정의 (124개 용어)
- **관계 관리**: 동의어, 연관용어, 계층 관계 (264개 관계)
- **다중 출력**: SQL, RDF/Cypher, Turtle 등 다양한 형식 지원
- **표준 연계**: DCAT-AP-KR, FIBO, SKOS 등 국제/국내 표준 매핑 (계획)

### 1.3 주요 통계 (v2.1)

| 항목 | 개수 | 비고 |
|------|------|------|
| 도메인 | 10개 | data.go.kr 16개 중 선별 |
| 분류 (MC_CLSF) | 175개 | 40개 중분류, 135개 소분류 |
| 용어 (MC_TERM) | 124개 | 도메인별 핵심 용어 |
| 용어 설명 | 173개 | enhanced_data.py에 정의 |
| 용어 관계 (MC_TERM_REL) | 264개 | 동의어 144개, 연관/계층 120개 |
| 동의어 | 144개 | REL_TYPE='S' |
| 연관/계층 관계 | 120개 | REL_TYPE='T' |

### 1.4 10개 도메인

| 코드 | 도메인 | 영문 | 디렉토리 | 기준 |
|------|--------|------|----------|------|
| 01 | 공공행정 | Public Administration | public/ | data.go.kr |
| 02 | 교육 | Education | - | data.go.kr |
| 03 | 보건의료 | Healthcare | medical/ | data.go.kr |
| 04 | 사회복지 | Social Welfare | - | data.go.kr |
| 05 | 법률 | Law | law/ | data.go.kr |
| 06 | 재정금융 | Finance | finance/ | data.go.kr |
| 07 | 산업경제 | Industry & Economy | commerce/ | data.go.kr |
| 08 | 재난안전 | Disaster & Safety | - | data.go.kr |
| 09 | 문화관광 | Culture & Tourism | - | data.go.kr |
| 10 | 환경기상 | Environment & Weather | - | data.go.kr |

---

## 2. 시스템 아키텍처

### 2.1 전체 아키텍처

```
┌─────────────────────────────────────────────────────────────┐
│                     입력 레이어 (Input)                       │
├─────────────────────────────────────────────────────────────┤
│  context.txt          │  사람이 읽고 편집하기 편한 텍스트      │
│  enhanced_data.py     │  상세 설명, 동의어, 관계 정의          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    처리 레이어 (Processing)                   │
├─────────────────────────────────────────────────────────────┤
│  build_enhanced_json.py  │  텍스트 → JSON 변환                │
│  generate.py             │  JSON → 다중 출력 생성              │
│  validate_ontology.py    │  구조적 정합성 검증                │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  마스터 데이터 (Master Data)                  │
├─────────────────────────────────────────────────────────────┤
│  context.json         │  모든 데이터의 원천 (JSON)            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    출력 레이어 (Output)                       │
├─────────────────────────────────────────────────────────────┤
│  SQL 출력             │  ontology.sql (통합)                  │
│                       │  mc_clsf_generated.sql (분류)         │
│                       │  mc_term_generated.sql (용어)         │
│                       │  mc_term_rel_generated.sql (관계)     │
├───────────────────────┼───────────────────────────────────────┤
│  그래프 DB 출력       │  context.cypher (Memgraph)            │
├───────────────────────┼───────────────────────────────────────┤
│  텍스트 출력          │  context_generated.txt (최소화)       │
├───────────────────────┼───────────────────────────────────────┤
│  RDF 출력 (계획)      │  context.ttl (Turtle)                 │
│                       │  context_skos.ttl (SKOS)              │
└─────────────────────────────────────────────────────────────┘
```

### 2.2 레이어 설명

#### 입력 레이어
- **context.txt**: 분류 및 용어의 기본 구조 정의 (ID, 이름, 영문명, 약어)
- **enhanced_data.py**: Python 딕셔너리로 상세 정보 정의
  - `CLASSIFICATION_README`: 분류별 상세 설명
  - `TERM_DESCRIPTIONS`: 용어별 상세 설명
  - `TERM_SYNONYMS`: 용어별 동의어 목록
  - `TERM_RELATED`: 용어 간 연관 관계
  - `TERM_HIERARCHY`: 용어 계층 구조

#### 처리 레이어
- **build_enhanced_json.py**: context.txt를 파싱하여 enhanced_data.py의 정보를 병합, context.json 생성
- **generate.py**: context.json을 읽어 SQL, Cypher, TXT 등 다양한 형식으로 출력 생성
- **validate_ontology.py**: JSON-SQL-TXT 간 3-way 일치성 검증

#### 마스터 데이터
- **context.json**: 모든 정보를 포함하는 JSON 형식의 마스터 파일

#### 출력 레이어
- SQL, Cypher, Turtle 등 다양한 형식의 출력 파일 자동 생성

---

## 3. 데이터 모델

### 3.1 데이터베이스 스키마

#### MC_CLSF (분류 테이블)

| 컬럼명 | 타입 | 설명 | 제약조건 |
|--------|------|------|----------|
| CLSF_ID | VARCHAR2(32) | 분류 ID | PRIMARY KEY |
| CLSF_NAME | VARCHAR2(500) | 분류명 | NOT NULL |
| CLSF_DESC | VARCHAR2(4000) | 분류 설명 | |
| PRT_CLSF_ID | VARCHAR2(32) | 상위 분류 ID | FOREIGN KEY |
| GROUP_YN | CHAR(1) | 그룹 여부 (Y/N) | DEFAULT 'N' |
| DELETE_YN | CHAR(1) | 삭제 여부 (Y/N) | DEFAULT 'N' |
| README | CLOB | 상세 설명 | |

**루트 분류 ID**: `03facd74b2d24f7cab807b8980391649`

#### MC_TERM (용어 테이블)

| 컬럼명 | 타입 | 설명 | 제약조건 |
|--------|------|------|----------|
| TERM_ID | VARCHAR2(32) | 용어 ID | PRIMARY KEY |
| TERM_NAME | VARCHAR2(500) | 한글명 | NOT NULL |
| TERM_NAME_EN | VARCHAR2(500) | 영문명 | |
| ACRONYM | VARCHAR2(100) | 약어 | |
| TERM_DESC | VARCHAR2(4000) | 용어 설명 | |
| DIC_ID | VARCHAR2(32) | 사전 ID | NOT NULL |
| TERM_TYPE | CHAR(1) | 용어 유형 | DEFAULT 'T' |
| DELETE_YN | CHAR(1) | 삭제 여부 (Y/N) | DEFAULT 'N' |
| README | CLOB | 연결 분류 ID | |

**사전 루트 ID**: `4147179070a84d3887b97eb57085d850`

**변경 내역 (v2.1)**:
- ❌ `PRT_TERM_ID` 제거 (용어 계층 구조는 MC_TERM_REL로 이동)
- ✅ `DIC_ID` 추가 (사전 관리용)

#### MC_TERM_REL (용어 관계 테이블) ✨ 신규 (v2.1)

| 컬럼명 | 타입 | 설명 | 제약조건 |
|--------|------|------|----------|
| TERM_ID | VARCHAR2(32) | 용어 ID | NOT NULL |
| REL_TYPE | CHAR(1) | 관계 유형 | NOT NULL |
| REL_TERM_ID | VARCHAR2(32) | 관계 대상 | NOT NULL |

**REL_TYPE 값**:
- `'S'`: Synonym (동의어) - REL_TERM_ID에 동의어 텍스트 저장
- `'T'`: Related/Hierarchy (연관용어 또는 계층) - REL_TERM_ID에 용어 ID 저장

**복합 키**: (TERM_ID, REL_TYPE, REL_TERM_ID)

#### MC_STD_MAPPING (표준 매핑 테이블) 🚧 계획중

| 컬럼명 | 타입 | 설명 | 제약조건 |
|--------|------|------|----------|
| MAPPING_ID | VARCHAR2(32) | 매핑 ID | PRIMARY KEY |
| STD_TYPE | VARCHAR2(50) | 표준 타입 | NOT NULL |
| MC_ID | VARCHAR2(32) | MC ID (분류/용어) | NOT NULL |
| MC_TYPE | CHAR(1) | MC 타입 (C/T) | NOT NULL |
| STD_URI | VARCHAR2(500) | 표준 온톨로지 URI | NOT NULL |
| MAPPING_TYPE | VARCHAR2(50) | 매핑 타입 | |
| CONFIDENCE | NUMBER(3,2) | 신뢰도 (0.0-1.0) | |
| NOTES | VARCHAR2(1000) | 매핑 근거 | |
| CREATED_DT | DATE | 생성일시 | DEFAULT SYSDATE |

**STD_TYPE 값**: 'DCAT-AP-KR', 'FIBO', 'SKOS', 'SCHEMA.ORG', 'DCTERMS'
**MAPPING_TYPE 값**: 'exactMatch', 'closeMatch', 'relatedMatch', 'broadMatch', 'narrowMatch'

### 3.2 ID 체계

#### 분류 ID (CLSF_ID)
```
C + DD(도메인) + LL(중분류) + SSSS(일련번호)
```
- 총 9자리: `C` + 2자리 도메인 + 2자리 중분류 + 4자리 일련번호
- 예시:
  - `C01000001`: 도메인 01 (공공행정) 최상위
  - `C01010001`: 도메인 01, 중분류 01, 일련번호 0001
  - `C06010001`: 도메인 06 (재정금융), 중분류 01, 일련번호 0001

#### 용어 ID (TERM_ID)
```
T + DD(도메인) + LL(중분류) + SSSS(일련번호)
```
- 총 9자리: `T` + 2자리 도메인 + 2자리 중분류 + 4자리 일련번호
- 예시:
  - `T06010001`: 도메인 06 (재정금융), 중분류 01, 일련번호 0001 (기준금리)
  - `T03050002`: 도메인 03 (보건의료), 중분류 05, 일련번호 0002 (대장암)

### 3.3 그래프 데이터 모델 (Memgraph)

#### 노드 타입
- `:Classification` - 분류 노드
- `:Term` - 용어 노드
- `:Synonym` - 동의어 노드

#### 관계 타입
- `:PARENT_OF` - 계층 관계 (분류↔분류, 용어↔용어)
- `:BELONGS_TO` - 용어가 분류에 속함
- `:SYNONYM_OF` - 용어의 동의어
- `:RELATED_TO` - 용어 간 연관 관계

#### 노드 속성
- `display_name` - 모든 노드에 `이름 (:라벨)` 형식
  - 예: `'공공행정 (:Classification)'`, `'기준금리 (:Term)'`, `'CRC (:Synonym)'`

---

## 4. 파일 구조

### 4.1 디렉토리 구조

```
ontology/
├── context.txt                      # 마스터 텍스트 (수동 편집)
├── enhanced_data.py                 # 상세 정보 정의 (수동 편집)
├── context.json                     # 마스터 JSON (자동 생성)
│
├── build_enhanced_json.py           # TXT → JSON 변환
├── generate.py                      # JSON → 출력 생성
├── validate_ontology.py             # 검증 스크립트
│
├── mc_clsf_generated.sql            # 분류 SQL (자동 생성)
├── mc_term_generated.sql            # 용어 SQL (자동 생성)
├── mc_term_rel_generated.sql        # 관계 SQL (자동 생성)
├── ontology.sql                     # 통합 SQL (자동 생성)
├── context.cypher                   # Memgraph Cypher (자동 생성)
├── context_generated.txt            # 최소화 텍스트 (자동 생성)
│
├── README.md                        # 프로젝트 소개
├── PROJECT_SPECIFICATION.md         # 프로젝트 명세서 (본 문서)
├── STANDARD_MAPPING_PLAN.md         # 표준 매핑 계획
├── context_schema.md                # JSON 스키마 설명
├── domain_mapping.md                # 도메인 매핑 계획
├── datagoKr_classification_analysis.md  # 데이터셋 분석
├── README_memgraph.md               # Memgraph 사용법
│
├── backup_20251201/                 # v2.0 백업
│   ├── context_v2.txt
│   ├── context.json
│   ├── enhanced_data.py
│   └── build_enhanced_json.py
│
└── (deprecated files)
    ├── context.xlsx                 # 더 이상 사용 안 함
    ├── build_context_json.py        # 구버전
    ├── generate_sql.py              # generate.py로 통합
    └── generate_cypher.py           # generate.py로 통합
```

### 4.2 파일 분류

#### 마스터 데이터 (수동 편집)
- `context.txt` - 분류 및 용어 기본 구조
- `enhanced_data.py` - 상세 설명, 동의어, 관계

#### 생성 파일 (자동 생성, 편집 금지)
- `context.json` - 마스터 JSON
- `*.sql` - SQL INSERT 문
- `context.cypher` - Memgraph 쿼리
- `context_generated.txt` - 최소화 텍스트

#### 스크립트
- `build_enhanced_json.py` - JSON 생성기
- `generate.py` - 출력 생성기
- `validate_ontology.py` - 검증기

#### 문서
- `README.md` - 프로젝트 소개
- `PROJECT_SPECIFICATION.md` - 프로젝트 명세 (본 문서)
- `STANDARD_MAPPING_PLAN.md` - 표준 매핑 계획
- 기타 분석 문서

---

## 5. 데이터 흐름

### 5.1 전체 흐름

```
┌──────────────┐
│ context.txt  │ ←─── 수동 편집 (기본 구조)
└──────┬───────┘
       │
       ├──────────────────────────────┐
       │                              │
┌──────▼────────┐              ┌──────▼────────────┐
│enhanced_data.py│ ←─── 수동 편집 (상세 정보)
└──────┬────────┘              └───────────────────┘
       │
       │ build_enhanced_json.py
       ▼
┌──────────────┐
│context.json  │ ◄─── 마스터 데이터
└──────┬───────┘
       │
       │ generate.py
       ├──────────────┬──────────────┬──────────────┐
       ▼              ▼              ▼              ▼
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│ontology  │  │context   │  │context_  │  │(future)  │
│.sql      │  │.cypher   │  │generated │  │.ttl      │
│(통합)    │  │(Memgraph)│  │.txt      │  │(RDF)     │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
```

### 5.2 작업 워크플로우

#### 새 분류 추가
```bash
# 1. context.txt 편집
vim context.txt
# 새 분류 ID 및 이름 추가 (ID 체계 준수)

# 2. enhanced_data.py 편집
vim enhanced_data.py
# CLASSIFICATION_README에 상세 설명 추가

# 3. 재생성
python3 build_enhanced_json.py  # context.json 생성
python3 generate.py             # 모든 출력 생성

# 4. 검증
python3 validate_ontology.py
```

#### 새 용어 추가
```bash
# 1. context.txt 편집
vim context.txt
# 새 용어 ID, 한글명, 영문명, 약어 추가

# 2. enhanced_data.py 편집
vim enhanced_data.py
# TERM_DESCRIPTIONS: 상세 설명
# TERM_SYNONYMS: 동의어 (선택)
# TERM_RELATED: 연관 용어 (선택)
# TERM_HIERARCHY: 계층 구조 (선택)

# 3. 재생성
python3 build_enhanced_json.py
python3 generate.py

# 4. 검증
python3 validate_ontology.py
```

---

## 6. API 및 인터페이스

### 6.1 Python 스크립트 인터페이스

#### build_enhanced_json.py

```python
# 실행
python3 build_enhanced_json.py

# 입력
- context.txt (필수)
- enhanced_data.py (필수)

# 출력
- context.json

# 주요 함수
parse_context_txt(filepath: str) -> Dict
parse_classifications(text: str, domain: Dict)
parse_terms(text: str, domain: Dict)
build_hierarchy(flat_list: List[Dict]) -> List[Dict]
```

#### generate.py

```python
# 실행
python3 generate.py

# 입력
- context.json (필수)

# 출력
- context_generated.txt
- mc_clsf_generated.sql
- mc_term_generated.sql
- mc_term_rel_generated.sql
- ontology.sql
- context.cypher

# 주요 함수
load_context_json(filepath: str) -> Dict
generate_context_txt(data: Dict) -> str
generate_mc_clsf_sql(data: Dict) -> str
generate_mc_term_sql(data: Dict) -> str
generate_mc_term_rel_sql(data: Dict) -> str
generate_context_cypher(data: Dict) -> str
```

#### validate_ontology.py

```python
# 실행
python3 validate_ontology.py

# 입력
- context.json
- ontology.sql
- context_generated.txt

# 검증 항목
- JSON-SQL-TXT 3-way 일치
- ID 유일성 및 형식
- 부모 ID 유효성
- 순환 참조 검사
- 필드 값 일치

# 출력
- 검증 결과 (콘솔)
- 오류, 경고, 정보 메시지
```

### 6.2 enhanced_data.py 구조

```python
# 분류별 상세 설명
CLASSIFICATION_README = {
    'C06010001': '통화정책 및 통화신용정책...',
    # ...
}

# 용어별 상세 설명
TERM_DESCRIPTIONS = {
    'T06010001': '중앙은행이 금융기관과 거래할 때...',
    # ...
}

# 용어별 동의어
TERM_SYNONYMS = {
    'T06010001': ['정책금리', 'Base Rate', '기준금리'],
    # ...
}

# 용어 간 연관 관계
TERM_RELATED = {
    'T06010001': ['T06010002', 'T06010003'],
    # ...
}

# 용어 계층 구조 (자식 → 부모)
TERM_HIERARCHY = {
    'T06010007': 'T06010003',  # 통화안정증권 → 공개시장운영
    # ...
}
```

---

## 7. 출력 형식

### 7.1 SQL 출력

#### ontology.sql (통합)

```sql
-- MC 분류·용어 통합 SQL
-- Generated: 2025-12-01

-- ==================== MC_CLSF (분류) ====================
INSERT INTO MC_CLSF (CLSF_ID, CLSF_NAME, CLSF_DESC, PRT_CLSF_ID, GROUP_YN, README)
VALUES ('C06000001', '재정금융', '금융 부문 정책...', '03facd74...', 'Y', '...');

-- ==================== MC_TERM (용어) ====================
INSERT INTO MC_TERM (TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM, TERM_DESC, DIC_ID, README)
VALUES ('T06010001', '기준금리', 'Base Rate', '', '중앙은행이...', '4147179...', 'C06010001');

-- ==================== MC_TERM_REL (용어 관계) ====================
-- 동의어 (Synonyms)
INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID)
VALUES ('T06010001', 'S', '정책금리');

-- 연관 용어 (Related Terms)
INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID)
VALUES ('T06010001', 'T', 'T06010002');

-- 계층 구조 (Hierarchy)
INSERT INTO MC_TERM_REL (TERM_ID, REL_TYPE, REL_TERM_ID)
VALUES ('T06010007', 'T', 'T06010003');
```

### 7.2 Cypher 출력 (Memgraph)

```cypher
// MC 분류·용어 Memgraph Cypher
// Generated: 2025-12-01

// Root Nodes
CREATE (:Classification {id: '03facd74...', name: 'ROOT', display_name: 'ROOT (:Classification)'});
CREATE (:Term {id: '4147179...', name_ko: 'ROOT', name_en: 'ROOT', display_name: 'ROOT (:Term)'});

// Classifications
CREATE (:Classification {
    id: 'C06010001',
    name: '통화정책',
    description: '통화정책 및 통화신용정책...',
    display_name: '통화정책 (:Classification)',
    readme: '...',
    group: false
});

// Classification Hierarchy
MATCH (p:Classification {id: 'C06000001'}), (c:Classification {id: 'C06010001'})
CREATE (p)-[:PARENT_OF]->(c);

// Terms
CREATE (:Term {
    id: 'T06010001',
    name_ko: '기준금리',
    name_en: 'Base Rate',
    acronym: '',
    description: '중앙은행이...',
    display_name: '기준금리 (:Term)'
});

// Term-Classification Relations
MATCH (t:Term {id: 'T06010001'}), (c:Classification {id: 'C06010001'})
CREATE (t)-[:BELONGS_TO]->(c);

// Synonym Relations
MATCH (t:Term {id: 'T06010001'})
CREATE (t)-[:SYNONYM_OF]->(:Synonym {value: '정책금리', display_name: '정책금리 (:Synonym)'});

// Related Term Relations
MATCH (t1:Term {id: 'T06010001'}), (t2:Term {id: 'T06010002'})
CREATE (t1)-[:RELATED_TO]->(t2);
```

### 7.3 RDF/Turtle 출력 (계획)

```turtle
@prefix mc: <http://mc.ontology.kr/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dct: <http://purl.org/dc/terms/> .

# ConceptScheme
mc:scheme a skos:ConceptScheme ;
    skos:prefLabel "MC 분류·용어 통합 체계"@ko ;
    skos:prefLabel "MC Classification and Terminology System"@en ;
    dct:created "2024-11-30" ;
    dct:modified "2025-12-01" ;
    dct:hasVersion "2.1.0" .

# Classification as Concept
mc:C06010001 a skos:Concept ;
    skos:prefLabel "통화정책"@ko ;
    skos:prefLabel "Monetary Policy"@en ;
    skos:definition "통화정책 및 통화신용정책..."@ko ;
    skos:broader mc:C06000001 ;
    skos:inScheme mc:scheme .

# Term as Concept
mc:T06010001 a skos:Concept ;
    skos:prefLabel "기준금리"@ko ;
    skos:prefLabel "Base Rate"@en ;
    skos:altLabel "정책금리"@ko ;
    skos:definition "중앙은행이..."@ko ;
    skos:related mc:T06010002, mc:T06010003 ;
    skos:inScheme mc:scheme .
```

---

## 8. 품질 관리

### 8.1 검증 프로세스

#### 자동 검증 (validate_ontology.py)

```bash
python3 validate_ontology.py
```

**검증 항목:**
1. ✅ JSON-SQL-TXT 3-way 일치
   - 분류/용어 개수 일치
   - ID 목록 일치
   - 필드 값 일치

2. ✅ ID 유일성 및 형식
   - 중복 ID 검사
   - ID 형식 검증 (C/T + 8자리)

3. ✅ 부모 ID 유효성
   - 모든 부모 ID가 존재하는지 확인
   - 루트 ID 검증

4. ✅ 순환 참조 검사
   - 분류 계층에 순환 참조 없음
   - 용어 계층에 순환 참조 없음

5. ✅ 필수 필드 존재
   - 모든 필수 필드 값 존재 확인

**검증 결과 (v2.1):**
```
============================================================
구조적 정합성 검증 결과
============================================================

[정보]
ℹ️  INFO: JSON 분류: 175개
ℹ️  INFO: SQL 분류: 175개
ℹ️  INFO: TXT 분류: 175개
ℹ️  INFO: JSON 용어: 124개
ℹ️  INFO: SQL 용어: 124개
ℹ️  INFO: TXT 용어: 124개

✅ 모든 검증 통과!

============================================================
총계: 0 오류, 0 경고, 6 정보
============================================================
```

### 8.2 품질 지표

| 지표 | 값 | 목표 |
|------|-----|------|
| ID 유일성 | 100% | 100% |
| 용어 설명 완성도 | 139.5% (173/124) | 100% |
| 동의어 커버리지 | 40.3% (50/124) | 50% |
| 연관 관계 밀도 | 0.66 (82/124) | 0.5 |
| 검증 통과율 | 100% | 100% |

### 8.3 코드 품질

- **Python 버전**: Python 3.7+
- **인코딩**: UTF-8
- **타입 힌팅**: typing 모듈 사용
- **에러 처리**: 명시적 예외 처리
- **주석**: 함수별 docstring 작성

---

## 9. 버전 이력

### v2.1.0 (2025-12-02)

**주요 변경사항:**
- ✨ MC_TERM_REL 테이블 신규 추가 (동의어, 연관용어, 계층 관계 분리)
- 🔄 MC_TERM 테이블 변경: PRT_TERM_ID → DIC_ID
- 📊 용어 설명 대폭 보강: 111개 → 173개 (+62개)
- 🔗 동의어 확장: 28개 → 144개 (+116개, 5배 증가)
- 🔗 연관 관계 확장: 20개 → 82개 (+62개, 4배 증가)
- 🔗 계층 구조 확장: 9개 → 49개 (+40개, 5배 증가)
- 📄 표준 온톨로지 연계 계획 수립 (DCAT-AP-KR, FIBO, SKOS)
- 📝 프로젝트 명세서 작성 (PROJECT_SPECIFICATION.md)

**통계:**
- 10개 도메인
- 175개 분류
- 124개 용어
- 264개 관계 (144개 동의어 + 120개 연관/계층)

### v2.0.0 (2025-12-01)

**주요 변경사항:**
- 🔄 도메인 재구성: 7개 → 10개 (data.go.kr 기반)
- 📋 data.go.kr 표준 16개 중 10개 선별
- 🆔 ID 매핑 및 마이그레이션
- 📊 분류 확장: 90개 → 92개

**도메인 변경:**
- 01 공공 → 01 공공행정
- 02 금융 → 06 재정금융
- 03 커머스 → 07 산업경제
- 07 의료 → 03 보건의료
- 신규: 02 교육, 04 사회복지, 05 법률, 08 재난안전, 09 문화관광, 10 환경기상

### v1.0.0 (2024-11-30)

**초기 버전:**
- 🎉 7개 도메인
- 📊 90개 분류
- 📝 116개 용어
- 🔗 기본 관계 정의

---

## 10. 향후 계획

### 10.1 표준 온톨로지 연계 (Phase 1-5)

**목표**: DCAT-AP-KR, FIBO, SKOS 등 국제/국내 표준과 연계

**타임라인**: 7-10주

**Phase 1: 설계 및 모델링** (1-2주)
- MC_STD_MAPPING 테이블 설계
- enhanced_data_mapping.py 구조 설계
- 우선순위 결정

**Phase 2: 매핑 데이터 정의** (2-3주)
- SKOS 매핑 (전체)
- DCAT-AP-KR 매핑 (분류)
- FIBO 매핑 (재정금융 도메인)

**Phase 3: 구현** (2-3주)
- generate_rdf.py 작성
- mc_std_mapping_generated.sql 생성
- context.ttl, context_skos.ttl 생성

**Phase 4: 검증 및 테스트** (1주)
- validate_mappings.py 작성
- SPARQL 쿼리 테스트

**Phase 5: 문서화 및 배포** (1주)
- MAPPING_GUIDE.md 작성
- STANDARDS.md 작성
- README 업데이트

**예상 산출물:**
- SQL: mc_std_mapping_generated.sql
- RDF: context.ttl, context_skos.ttl, context_dcat.ttl, context_fibo.ttl
- Python: enhanced_data_mapping.py, generate_rdf.py, validate_mappings.py
- 문서: MAPPING_GUIDE.md, STANDARDS.md

**상세 계획**: [STANDARD_MAPPING_PLAN.md](STANDARD_MAPPING_PLAN.md) 참조

### 10.2 SPARQL 엔드포인트 (Phase 6)

**목표**: SPARQL 쿼리 서비스 제공

**계획:**
- Apache Jena Fuseki 또는 Virtuoso 설치
- RDF 데이터 로드
- SPARQL 엔드포인트 구성
- 웹 인터페이스 제공

**엔드포인트**: `http://mc.ontology.kr/sparql` (계획)

### 10.3 웹 인터페이스 (Phase 7)

**목표**: 온톨로지 브라우저 및 검색 기능

**기능:**
- 분류 트리 브라우저
- 용어 검색
- 관계 시각화
- SPARQL 쿼리 빌더
- RDF/Turtle 다운로드

### 10.4 API 서버 (Phase 8)

**목표**: RESTful API 제공

**엔드포인트:**
```
GET /api/classifications
GET /api/classifications/{id}
GET /api/terms
GET /api/terms/{id}
GET /api/terms/{id}/synonyms
GET /api/terms/{id}/related
GET /api/search?q={query}
```

### 10.5 확장 계획

- **도메인 추가**: 필요시 새 도메인 추가
- **다국어 지원**: 영문 설명 보강
- **버전 관리**: Git 기반 변경 이력 관리
- **커뮤니티**: GitHub 이슈 관리, 기여 가이드 작성

---

## 부록

### A. 참고 자료

- **data.go.kr**: https://www.data.go.kr
- **DCAT-AP**: https://www.w3.org/TR/vocab-dcat-2/
- **FIBO**: https://spec.edmcouncil.org/fibo/
- **SKOS**: https://www.w3.org/2004/02/skos/
- **Memgraph**: https://memgraph.com/docs

### B. 관련 문서

- [README.md](README.md) - 프로젝트 소개
- [CLAUDE.md](../CLAUDE.md) - Claude Code 작업 가이드
- [STANDARD_MAPPING_PLAN.md](STANDARD_MAPPING_PLAN.md) - 표준 매핑 계획
- [context_schema.md](context_schema.md) - JSON 스키마
- [domain_mapping.md](domain_mapping.md) - 도메인 매핑
- [datagoKr_classification_analysis.md](datagoKr_classification_analysis.md) - 데이터셋 분석
- [README_memgraph.md](README_memgraph.md) - Memgraph 사용법

### C. 연락처

- **프로젝트**: MC Classification and Terminology Integration System
- **버전**: 2.1.0
- **마지막 업데이트**: 2025-12-02

---

**문서 버전**: 1.0
**작성일**: 2025-12-02
**작성자**: MC Ontology Team
