# MC 분류·용어 통합 체계

**버전:** 3.6.0
**최종 업데이트:** 2025-12-10
**구조:** 단일 마스터 파일 (ontology.json)

[![License](https://img.shields.io/badge/license-CC--BY--4.0-blue.svg)](http://creativecommons.org/licenses/by/4.0/)
[![Version](https://img.shields.io/badge/version-3.6.0-green.svg)](README.md)
[![Data Source](https://img.shields.io/badge/source-data.go.kr-orange.svg)](https://www.data.go.kr)

## 개요

문서 분류 및 용어 관리를 위한 체계적인 온톨로지 시스템입니다. 공공데이터포털(data.go.kr)의 16개 표준 분류체계 중 12개를 선별하고, 20개 국제/국내 표준과 연계했습니다.

**주요 특징:**
- 📄 **단일 마스터**: ontology.json 하나가 모든 데이터의 원천
- 🏛️ **표준 기반**: 20개 국제/국내 표준 연계 (SKOS, ISO25964, UNESCO 등)
- 📊 **풍부한 관계**: 237개 용어 관계 + 255개 표준 레퍼런스
- 🔄 **다중 출력**: SQL, Cypher, JSON, TXT 자동 생성
- ✅ **높은 품질**: 자동 검증 (0 오류, 0 경고)

## 통계 (v3.6)

| 항목 | 개수 |
|------|------|
| 도메인 | 12개 |
| 분류 | 376개 (44개 중분류, 332개 소분류) |
| 용어 | 221개 |
| 동의어 관계 | 154개 |
| 연관 용어 관계 | 83개 |
| 표준 레지스트리 | 20개 |
| 표준 레퍼런스 | 255개 (분류 105개, 용어 150개) |

## 12개 도메인

1. **01 공공행정** (Public Administration)
2. **02 교육** (Education)
3. **03 보건의료** (Healthcare)
4. **04 사회복지** (Social Welfare)
5. **05 법률** (Law)
6. **06 재정금융** (Finance)
7. **07 산업경제** (Industry & Economy)
8. **08 재난안전** (Disaster & Safety)
9. **09 문화관광** (Culture & Tourism)
10. **10 환경기상** (Environment & Weather)
11. **11 과학기술** (Science & Technology)
12. **12 국토교통** (Land & Transport)

## 파일 구조

### 마스터 파일
- **ontology.json** - 모든 데이터의 단일 원천 (376개 분류, 221개 용어, 표준 레퍼런스 포함)

### 스크립트
- **generate.py** - ontology.json → generated/ 디렉토리에 모든 출력 파일 생성
- **validate_ontology.py** - 구조적 정합성 검증

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

### MC_TERM_REL (용어 관계)
```sql
TERM_ID     VARCHAR2(32)   -- 용어 ID
REL_TYPE    CHAR(1)        -- 관계 유형 ('S': 동의어, 'T': 연관/계층)
REL_TERM_ID VARCHAR2(32)   -- 관계 대상
```

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

## 표준 레지스트리 (20개)

### 국제 표준 (8개)
- **STD-SKOS** - Simple Knowledge Organization System
- **STD-ISO25964** - Thesauri and interoperability
- **STD-DC** - Dublin Core Metadata Terms
- **STD-UNESCO** - UNESCO Thesaurus
- **STD-OECD-FOS** - OECD Fields of Science
- **STD-FIBO** - Financial Industry Business Ontology
- **STD-MESH** - Medical Subject Headings
- **STD-ICD11** - International Classification of Diseases

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
- `:PARENT_OF` - 계층 관계
- `:BELONGS_TO` - 용어→분류
- `:SYNONYM_OF` - 동의어
- `:RELATED_TO` - 연관 관계

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
```

## 검증

### 검증 항목
- ✅ JSON-SQL-TXT 3-way 일치
- ✅ ID 유일성 및 형식
- ✅ 부모 ID 유효성
- ✅ 순환 참조 검사
- ✅ 필드 값 일치
- ✅ 표준 레퍼런스 유효성

### 검증 결과 (v3.6)
```bash
$ python3 validate_ontology.py

✅ 모든 검증 통과!
총계: 0 오류, 0 경고, 9 정보
```

## 버전 이력

### v3.6 (2025-12-10)
- 🎯 **단일 마스터 구조**: ontology.json 하나로 통합
- 🗂️ **파일 정리**: archive/ 디렉토리 분리
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
