# MC 분류·용어 통합 체계

**버전:** 3.13.0
**최종 업데이트:** 2025-12-11
**구조:** 단일 마스터 파일 (ontology.json)

[![License](https://img.shields.io/badge/license-CC--BY--4.0-blue.svg)](http://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-3.13.0-green.svg)](README.md)
[![Data Source](https://img.shields.io/badge/source-data.go.kr-orange.svg)](https://www.data.go.kr)

## 개요

문서 분류 및 용어 관리를 위한 체계적인 온톨로지 시스템입니다. 공공데이터포털(data.go.kr)의 16개 표준 분류체계 중 12개를 선별하고, 24개 국제/국내 표준과 연계했습니다.

**주요 특징:**
- 📄 **단일 마스터**: ontology.json 하나가 모든 데이터의 원천
- 🏛️ **표준 기반**: 24개 국제/국내 표준 연계 (SKOS, GS1, arXiv, ACM CCS 등)
- 📊 **SKOS 기반 SYNONYM**: 5가지 타입 (Exact/Close/Related/Broader/Narrower)
- 🔄 **다중 출력**: SQL, Cypher, JSON, TXT, Excel 자동 생성
- ✅ **높은 품질**: 자동 검증 (0 오류, 0 경고)

## 통계 (v3.13)

| 항목 | 개수 | 변경 |
|------|------|------|
| 도메인 | 12개 | - |
| 분류 | 376개 (44개 중분류, 332개 소분류) | - |
| **용어** | **440개** | **+219 (공통표준용어 연계)** |
| **동의어 (총계)** | **470개** | - |
| └ Term → Term | 5개 | - |
| └ Exact (완전 동의어) | 41개 | - |
| └ Close (유사어) | 6개 | - |
| └ Related (관련어) | 366개 | - |
| └ Broader (상위 개념) | 12개 | - |
| └ Narrower (하위 개념) | 40개 | - |
| 연관 용어 (RELATED_TO) | 78개 | - |
| 분류 유사 관계 (SIMILAR_TO) | 42개 | - |
| 표준 레지스트리 | 24개 | - |
| **표준 레퍼런스** | **624개 (분류 255개, 용어 369개)** | **+219** |
| 분류 커버리지 | 232/376 (61.7%) | - |
| **용어 커버리지** | **359/440 (81.6%)** | **+18.3%p** |
| 동의어 커버리지 | 182/182 (100.0%) | - |

## 12개 도메인

1. **01 공공행정** (Public Administration)
2. **02 교육** (Education)
3. **03 보건의료** (Healthcare)
4. **04 사회복지** (Social Welfare)
5. **05 법률** (Law)
6. **06 재정금융** (Finance)
7. **07 산업경제** (Industry & Economy)
8. **08 디지털커머스** (Digital Commerce)
9. **09 문화관광** (Culture & Tourism)
10. **10 환경기상** (Environment & Weather)
11. **11 과학기술** (Science & Technology)
12. **12 재난안전** (Disaster & Safety)

## 파일 구조

### 마스터 파일
- **ontology.json** - 모든 데이터의 단일 원천 (376개 분류, 440개 용어, 표준 레퍼런스 포함)

### 스크립트
- **generate.py** - ontology.json → generated/ 디렉토리에 모든 출력 파일 생성
- **validate_ontology.py** - 구조적 정합성 검증
- **export_to_excel.py** - Excel 파일 생성 (분류, 용어, 동의어, 연관관계, 표준)
- **SYNONYM 관리 (v3.12):**
  - **analyze_synonym_types.py** - 동의어 타입 자동 분류
  - **suggest_close_matches.py** - Close Match 후보 추천
  - **apply_close_matches.py** - 고신뢰도 Close Match 자동 적용
  - **migrate_to_v312.py** - v3.11 → v3.12 마이그레이션

### 생성 디렉토리 (generated/)
자동 생성된 모든 파일이 저장됨 (수정 금지):
- **ontology.sql** - 통합 SQL (MC_CLSF + MC_TERM + MC_TERM_REL + MC_STD_REF)
- **ontology.txt** - 사람이 읽기 편한 텍스트
- **ontology.cypher** - Memgraph 그래프 DB 쿼리
- **mc_clsf_generated.sql** - 분류 테이블 SQL
- **mc_term_generated.sql** - 용어 테이블 SQL
- **mc_term_rel_generated.sql** - 용어 관계 테이블 SQL
- **mc_std_ref_generated.sql** - 표준 레퍼런스 테이블 SQL
- **standards_registry.json** - 표준 레지스트리 독립 파일

### 참고 문서
- **README_memgraph.md** - Memgraph 그래프 DB 사용법
- **context_schema.md** - JSON 스키마 상세 설명
- **SAMPLE_QUERIES.md** - Cypher/SQL 샘플 쿼리 (40개)
- **SYNONYM_REFINEMENT_PROPOSAL.md** - v3.12 SYNONYM 타입 세분화 설계 문서

### 생성 파일
- **ontology_master_data.xlsx** - Excel 마스터 데이터 (6개 시트)
- **selected_standard_terms.json** - 선별된 공통표준용어 (219개)
- **synonym_categories.json** - 자동 분류 결과 (465개)
- **close_match_suggestions.json** - Close Match 후보 (83개)

## 데이터 흐름

```
[마스터]
ontology.json
     ↓
generate.py
     ↓
generated/
├─ ontology.txt
├─ ontology.sql
├─ ontology.cypher
├─ mc_clsf_generated.sql
├─ mc_term_generated.sql
├─ mc_term_rel_generated.sql
├─ mc_std_ref_generated.sql
└─ standards_registry.json
```

## 빠른 시작

### 1. 분류/용어 추가

```bash
# ontology.json 직접 편집 (JSON 편집기 사용 권장)
vim ontology.json

# 모든 출력 파일 재생성
python3 generate.py

# 검증
python3 validate_ontology.py
```

### 2. 검증 실행

```bash
python3 validate_ontology.py
# ✅ 모든 검증 통과!
# 총계: 0 오류, 0 경고, 9 정보
```

## ID 체계

### 분류 ID (9자리)
```
C + DD(도메인) + LL(중분류) + SSSS(일련번호)
```
- 예: `C01010001` = 도메인 01 + 중분류 01 + 일련번호 0001

### 용어 ID (9자리)
```
T + DD(도메인) + LL(중분류) + SSSS(일련번호)
```
- 예: `T01010001` = 도메인 01 + 중분류 01 + 일련번호 0001

## 데이터베이스 스키마

### MC_CLSF (분류)
```sql
CLSF_ID     VARCHAR2(32)   -- 분류 ID
CLSF_NAME   VARCHAR2(500)  -- 분류명
CLSF_DESC   VARCHAR2(4000) -- 분류 설명
PRT_CLSF_ID VARCHAR2(32)   -- 상위 분류 ID
GROUP_YN    CHAR(1)        -- 그룹 여부
DELETE_YN   CHAR(1)        -- 삭제 여부
README      CLOB           -- 상세 설명
```

### MC_TERM (용어)
```sql
TERM_ID      VARCHAR2(32)   -- 용어 ID
TERM_NAME    VARCHAR2(500)  -- 한글명
TERM_NAME_EN VARCHAR2(500)  -- 영문명
ACRONYM      VARCHAR2(100)  -- 약어
TERM_DESC    VARCHAR2(4000) -- 용어 설명
DIC_ID       VARCHAR2(32)   -- 사전 ID
TERM_TYPE    CHAR(1)        -- 용어 유형
DELETE_YN    CHAR(1)        -- 삭제 여부
README       CLOB           -- 연결 분류 ID
```

### MC_TERM_REL (용어 관계) ← v3.12 확장
```sql
TERM_ID     VARCHAR2(32)   -- 용어 ID
REL_TYPE    VARCHAR2(2)    -- 관계 유형 (v3.12 확장)
REL_TERM_ID VARCHAR2(32)   -- 관계 대상
```

**REL_TYPE 코드 (v3.12 SKOS 기반):**
| 코드 | 타입 | 설명 | 개수 |
|------|------|------|------|
| `S` | Term → Term | 용어 간 동의어 | 5개 |
| `T` | Related | 연관 관계 | 78개 |
| `SE` | Exact Synonym | 완전 동의어 (약어, 영문명) | 41개 |
| `SC` | Close Synonym | 유사어 (혼용 가능) | 6개 |
| `SR` | Related Synonym | 관련어 | 366개 |
| `SB` | Broader | 상위 개념 | 12개 |
| `SN` | Narrower | 하위 개념 | 40개 |

### MC_STANDARD (표준 레지스트리)
```sql
STD_ID       VARCHAR2(32)   -- 표준 ID
STD_CODE     VARCHAR2(100)  -- 표준 코드
STD_NAME_KO  VARCHAR2(500)  -- 한글명
STD_NAME_EN  VARCHAR2(500)  -- 영문명
STD_TYPE     VARCHAR2(50)   -- 유형
STD_SCOPE    VARCHAR2(50)   -- 범위
ORGANIZATION VARCHAR2(500)  -- 발행기관
VERSION      VARCHAR2(100)  -- 버전
URI          VARCHAR2(2000) -- URI
STD_DESC     VARCHAR2(4000) -- 설명
```

### MC_CLSF_STD_REF (분류 표준 레퍼런스)
```sql
CLSF_ID       VARCHAR2(32)   -- 분류 ID
STD_ID        VARCHAR2(32)   -- 표준 ID
EXTERNAL_ID   VARCHAR2(500)  -- 외부 ID
EXTERNAL_NAME VARCHAR2(500)  -- 외부 명칭
MATCH_TYPE    VARCHAR2(50)   -- 매치 타입
CONFIDENCE    NUMBER(3,2)    -- 신뢰도 (0.0-1.0)
NOTE          VARCHAR2(4000) -- 비고
```

### MC_TERM_STD_REF (용어 표준 레퍼런스)
```sql
TERM_ID       VARCHAR2(32)   -- 용어 ID
STD_ID        VARCHAR2(32)   -- 표준 ID
EXTERNAL_ID   VARCHAR2(500)  -- 외부 ID
EXTERNAL_NAME VARCHAR2(500)  -- 외부 명칭
MATCH_TYPE    VARCHAR2(50)   -- 매치 타입
CONFIDENCE    NUMBER(3,2)    -- 신뢰도 (0.0-1.0)
NOTE          VARCHAR2(4000) -- 비고
```

## 표준 레지스트리 (24개)

### 국제 표준 (12개)
- **STD-SKOS** - Simple Knowledge Organization System
- **STD-ISO25964** - Thesauri and interoperability
- **STD-DC** - Dublin Core Metadata Terms
- **STD-UNESCO** - UNESCO Thesaurus
- **STD-OECD-FOS** - OECD Fields of Science
- **STD-FIBO** - Financial Industry Business Ontology
- **STD-MESH** - Medical Subject Headings
- **STD-ICD11** - International Classification of Diseases
- **STD-GS1** - GS1 eCommerce Standards (글로벌 유통·물류·전자상거래)
- **STD-SCHEMA** - Schema.org Structured Data (웹 구조화 데이터)
- **STD-ARXIV** - arXiv Subject Classification (과학 논문 분류)
- **STD-ACMCCS** - ACM Computing Classification System (컴퓨터과학 분류)

### 국내 표준 (6개)
- **STD-BRM** - 행정기관 업무참조모형
- **STD-KSIC** - 한국표준산업분류
- **STD-KCD** - 한국표준질병사인분류
- **STD-MOLEG** - 법제처 법령용어
- **STD-DATAGOkr** - 공공데이터포털 분류체계
- **STD-STDTERM** - 국립국어원 표준국어대사전

### 한국 응용 표준 (6개)
- **STD-DCAT-AP-KR** - 한국형 데이터 카탈로그 표준
- **STD-KOOR** - 한국온톨로지언어
- **STD-ADMCODE** - 행정구역코드
- **STD-KS-ISO11179** - 메타데이터 등록 표준
- **STD-DBSTD** - 공공데이터 DB표준화
- **STD-DATAQUALITY** - 공공데이터 품질관리 기준

## 매치 타입

- **EXACT_MATCH** - 정확한 일치 (개념 동일)
- **CLOSE_MATCH** - 밀접한 일치 (개념 유사)
- **BROAD_MATCH** - 상위 개념
- **NARROW_MATCH** - 하위 개념
- **RELATED_MATCH** - 연관 개념
- **DERIVED_FROM** - 파생

## 그래프 데이터베이스

### 노드 타입
- `:Classification` - 분류
- `:Term` - 용어
- `:Synonym` - 동의어

### 관계 타입

| 관계 | Source | Target | 방향 | 설명 |
|------|--------|--------|------|------|
| `:PARENT_OF` | Classification | Classification | 단방향 | 분류 계층 (376개) |
| `:PARENT_OF` | Term | Term | 단방향 | 용어 계층 (221개) |
| `:BELONGS_TO` | Term | Classification | 단방향 | 용어 소속 (221개) |
| `:SYNONYM_OF` | Term | Term | 양방향 | 용어 동의어 (5개 = 10개 관계) |
| `:RELATED_TO` | Term | Term | 양방향 | 연관 용어 (78개 = 156개 관계) |
| `:SIMILAR_TO` | Classification | Classification | 양방향 | 분류 유사 관계 (42개) |

**SYNONYM 관계 타입 (v3.12 SKOS 기반):**

| 관계 | 설명 | 개수 |
|------|------|------|
| **`:EXACT_SYNONYM`** | 완전 동의어 (약어, 영문명) | 41개 |
| **`:CLOSE_SYNONYM`** | 유사어 (혼용 가능한 근접 개념) | 6개 |
| **`:RELATED_SYNONYM`** | 관련어 (연관되지만 동의어 아님) | 366개 |
| **`:BROADER_THAN`** | 상위 개념 | 12개 |
| **`:NARROWER_THAN`** | 하위 개념 | 40개 |

**v3.12 주요 변경:**
- **SKOS 기반 SYNONYM 타입 세분화**: 5가지 관계 타입으로 분류
- **자동 분류 시스템**: 패턴 기반 465개 동의어 자동 분류
- **Close Match 추천**: 83개 후보 중 6개 고신뢰도(0.9+) 자동 적용

### Memgraph 사용법
```cypher
// 표준 레퍼런스가 있는 용어 조회
MATCH (t:Term)
WHERE exists(t.standard_refs)
RETURN t.name_ko, t.standard_refs;

// 특정 도메인의 분류
MATCH (c:Classification)
WHERE c.id STARTS WITH 'C01'
RETURN c;

// 계층 구조
MATCH path = (root:Classification)-[:PARENT_OF*]->(child)
WHERE root.id = 'C01000001'
RETURN path;

// v3.12: 타입별 동의어 검색
MATCH (t:Term)-[:EXACT_SYNONYM]->(s:Synonym)
WHERE t.name_ko = '공개시장운영'
RETURN s.value AS exact_synonym;

// v3.12: Close Match (유사어) 조회
MATCH (t:Term)-[:CLOSE_SYNONYM]->(s:Synonym)
RETURN t.name_ko, s.value AS close_synonym;

// v3.12: 상위/하위 개념 탐색
MATCH (t:Term)-[:BROADER_THAN]->(s:Synonym)
RETURN t.name_ko, s.value AS broader_concept;
```

## 검증

### 검증 항목
- ✅ JSON-SQL-TXT 3-way 일치
- ✅ ID 유일성 및 형식
- ✅ 부모 ID 유효성
- ✅ 순환 참조 검사
- ✅ 필드 값 일치
- ✅ 표준 레퍼런스 유효성

### 검증 결과 (v3.13)
```bash
$ python3 validate_ontology.py

✅ 모든 검증 통과!
총계: 0 오류, 0 경고, 9 정보
- JSON 분류: 376개, SQL 분류: 376개, TXT 분류: 376개
- JSON 용어: 440개, SQL 용어: 440개, TXT 용어: 440개
- 분류 표준 레퍼런스: 232개 (255개 매핑)
- 용어 표준 레퍼런스: 359개 (369개 매핑)
- 동의어: 470개 (5타입: SE 41, SC 6, SR 366, SB 12, SN 40)
```

## 버전 이력

### v3.13 (2025-12-11) - 현재 버전
- 🚀 **공통표준용어 연계**: 9,027개 공공데이터 표준용어 중 219개 선별 추가
- 📈 **용어 대폭 확장**: 221개 → 440개 (+219개, +99% 증가)
- 🎯 **용어 커버리지 향상**: 63.3% → 81.6% (+18.3%p)
- 📊 **표준 레퍼런스 자동 매핑**: STD-STDTERM 219개 (EXACT_MATCH, confidence 1.0)
- 🔧 **ID 생성 로직 강화**: 하위 용어(children) 재귀 체크, 충돌 완전 방지
- 🐛 **검증 스크립트 버그 수정**: 이스케이프 따옴표(`''`) 처리 개선
- 📋 **도메인별 균형 추가**: 25개씩 배분 (번호, 코드, 명, 일자 등 핵심 항목 우선)
- ✅ **검증 완료**: 0 errors, 0 warnings (JSON=440, SQL=440, TXT=440)

### v3.12 (2025-12-11)
- 🎯 **SKOS 기반 SYNONYM 타입 세분화**: 5가지 관계 타입
  - Exact (41개): 완전 동의어 (약어, 영문명)
  - Close (6개): 유사어 (혼용 가능한 근접 개념)
  - Related (366개): 관련어 (연관되지만 동의어 아님)
  - Broader (12개): 상위 개념
  - Narrower (40개): 하위 개념
- ✨ **자동 분류 시스템**: 패턴 기반 465개 동의어 자동 분류
- 🔍 **Close Match 추천 엔진**: 83개 후보 추출, 6개 고신뢰도(0.9+) 자동 적용
- 🔄 **SQL REL_TYPE 확장**: CHAR(1) → VARCHAR(2), SE/SC/SR/SB/SN 코드
- 📊 **Cypher 타입별 관계**: :EXACT_SYNONYM, :CLOSE_SYNONYM, :RELATED_SYNONYM, :BROADER_THAN, :NARROWER_THAN
- 📋 **Excel 출력 강화**: 타입별 동의어 시트
- 📝 **설계 문서**: SYNONYM_REFINEMENT_PROPOSAL.md

### v3.11 (2025-12-11)
- ✨ **하이브리드 SYNONYM 구조**: Term → Term (5개) + Term → Synonym node (465개)
- 🔄 **RELATED_TO 복원**: v3.9에서 78개 조건부 복원
- 🎯 **자기 참조 제거**: 15개 제거
- 📝 **정책 문서화**: term_revision_proposal.md

### v3.10 (2025-12-11)
- 🔄 **관계 재구조화**: SIMILAR_TO 추가, RELATED_TO 제거
- ✨ Classification 간 유사 관계 도입 (21쌍, 42개 관계)
- ✗ Term 간 RELATED_TO 제거 (79개) - SYNONYM_OF로 충분
- 🎯 도메인 간 연계 강화 (교육↔과학기술, 보건의료↔사회복지 등)
- 📊 총 관계 수: 1,453개 → 1,412개 (최적화)

### v3.9 (2025-12-11)
- 🎯 **디지털커머스·과학기술 표준 레퍼런스 완성**: 27.3%/25.9% → 81.8%/88.9%
- ✨ 4개 신규 표준 등록: GS1, Schema.org, arXiv, ACM CCS
- 📊 37개 표준 레퍼런스 추가 (29개 분류)
- 🏆 **전체 12개 도메인 모두 50%+ 달성**
- 📈 전체 분류 커버리지: 54.0% → 61.7%
- 🔧 검증 스크립트 개선: 동적 표준 ID 로드

### v3.8 (2025-12-11)
- 🎯 **동의어 대폭 확장**: 87개 → 485개 (+398개, 557% 증가)
- ✨ 148개 용어에 동의어 추가 (37개 → 182개)
- 🏆 **100% 동의어 커버리지 달성**: 182/182개 용어 (평균 2.66개/용어)
- 📊 도메인별 균형 있는 동의어 확장 (재난안전 60개, 법률 53개 등)
- 🔍 검색 성능 대폭 향상: 용어당 평균 0.48개 → 2.66개

### v3.7 (2025-12-10)
- 📊 **분류 표준 레퍼런스 대폭 확장**: 23.9% → 54.0% (+30.1%p)
- ✨ 113개 분류에 표준 매핑 추가 (90 → 203개)
- 🎯 목표 50% 초과 달성
- 🔗 7개 주요 표준 활용 (MESH, FIBO, UNESCO, KSIC, KCD, BRM 등)
- 📈 10개 도메인 50% 이상 달성

### v3.6 (2025-12-10)
- 🎯 **단일 마스터 구조**: ontology.json 하나로 통합
- 🗂️ **파일 정리**: archive/ 및 generated/ 디렉토리 분리
- 📝 **명명 일관성**: context.* → ontology.* 통일

### v3.5 (2025-12-10)
- 📊 용어 표준 레퍼런스 63% 달성 (140/221개)
- 🔗 66개 신규 용어 매핑 추가

### v3.0 (2025-12-08)
- ✨ 분류 대폭 확장: 175개 → 376개
- 🌐 도메인 확대: 10개 → 12개 (과학기술, 국토교통 추가)
- 📋 표준 레지스트리 구축: 20개 표준 등록
- 🔗 표준 레퍼런스 시스템 구현

### v2.1 (2025-12-01)
- 📊 세부 분류 확장: 92개 → 175개
- 🎯 data.go.kr 실제 데이터셋 200+ 개 분석

### v2.0 (2025-12-01)
- 🔄 도메인 재구성: 7개 → 10개

### v1.0 (2024-11-30)
- 🎉 초기 버전

## 라이선스

이 프로젝트는 공공데이터포털(data.go.kr)의 분류체계를 참고하여 만들어졌습니다.
