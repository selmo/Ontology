# CLAUDE.md

이 파일은 Claude Code (claude.ai/code)가 본 저장소에서 작업할 때 참고하는 가이드입니다.

## 저장소 개요

다양한 도메인의 참고 문서를 관리하는 **문서 저장소**입니다:

- **commerce/** - 이커머스 및 디지털 경제 관련 보고서
- **finance/** - 금융 정책 및 규제 문서
- **law/** - 법률 판례 및 세제 관련 문서
- **medical/** - 의료 및 건강 가이드라인 문서
- **public/** - 정부 부처 업무계획 및 정책 문서
- **ontology/** - 분류 및 용어 관리 체계 (표준 기반)

문서 형식: PDF, HWPX

## 온톨로지 체계

`ontology/` 디렉토리는 **단일 마스터 파일(ontology.json)** 기반의 체계적인 분류·용어 시스템을 포함합니다.

**버전:** 3.7.0
**구조:** 단일 마스터 (ontology.json)
**최종 업데이트:** 2025-12-10

### 빠른 참조

**통계 (v3.7):**
- 12개 도메인
- 376개 분류 (44개 중분류, 332개 소분류)
- 221개 용어
- 154개 동의어, 83개 연관관계
- 20개 표준 등록, 368개 표준 레퍼런스
  - **분류: 203개 (54.0%) - 218 레퍼런스** ⬆️
  - 용어: 140개 (63.3%) - 150 레퍼런스

**주요 작업:**
```bash
# ontology.json 편집 (JSON 편집기 사용 권장)
vim ontology.json

# 모든 출력 파일 재생성
python3 generate.py  # ontology.json → SQL/Cypher/TXT/JSON

# 검증
python3 validate_ontology.py  # 0 errors, 0 warnings
```

**파일 구조 (v3.6 단순화):**
- 📝 `ontology.json` → **마스터 파일 (단일 원천)**
- 📂 `generated/` → 자동 생성 파일 (ontology.sql, ontology.cypher, ontology.txt, *.sql 등)
- 📂 `archive/` → 구버전 파일 (context.txt, enhanced_data.py, standards_registry.py 등)

### 주요 파일

**마스터 파일:**
- `ontology.json` - **단일 원천**. 모든 분류, 용어, 표준 레퍼런스 포함 (369KB)

**스크립트:**
- `generate.py` - ontology.json → generated/ 디렉토리에 모든 출력 파일 생성
- `validate_ontology.py` - 구조적 정합성 검증 (10개 검증 항목)

**생성 디렉토리 (generated/):**
자동 생성된 파일 (수정 금지):
- `ontology.txt` - 사람이 읽기 편한 텍스트 (ID와 이름만)
- `ontology.sql` - 통합 SQL (MC_CLSF + MC_TERM + MC_TERM_REL + MC_STD_REF)
- `ontology.cypher` - Memgraph 그래프 쿼리
- `mc_clsf_generated.sql` - 분류 테이블 SQL
- `mc_term_generated.sql` - 용어 테이블 SQL
- `mc_term_rel_generated.sql` - 용어 관계 테이블 SQL
- `mc_std_ref_generated.sql` - 표준 레퍼런스 SQL
- `standards_registry.json` - 표준 레지스트리 JSON

**참고 문서:**
- `README.md` - 프로젝트 개요 및 사용법
- `README_memgraph.md` - Memgraph 사용법
- `context_schema.md` - JSON 스키마 상세

### 데이터 흐름

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

**v3.6 변경점:**
- ✅ 단일 마스터 파일 (`ontology.json`)
- ✅ 소스 파일 분리 제거 (context.txt, enhanced_data.py, standards_registry.py → archive/)
- ✅ 생성 파일 분리 (`generated/` 디렉토리)
- ✅ 데이터 동기화 불필요
- ✅ 명명 일관성 (context.* → ontology.*)

### ID 체계

**분류 ID (CLSF_ID)**
```
C + DD(도메인) + LL(중분류) + SSSS(일련번호)
```
- 총 9자리: `C` + 2자리 도메인 + 2자리 중분류 + 4자리 일련번호
- 예: `C01010001` = 도메인 01 + 중분류 01 + 일련번호 0001

**용어 ID (TERM_ID)**
```
T + DD(도메인) + LL(중분류) + SSSS(일련번호)
```
- 총 9자리: `T` + 2자리 도메인 + 2자리 중분류 + 4자리 일련번호
- 예: `T01010001` = 도메인 01 + 중분류 01 + 일련번호 0001

### 도메인 체계 (12개 도메인)

| 코드 | 도메인 | 영문 | 디렉토리 | 주요 표준 | 용어 커버리지 |
|------|--------|------|----------|-----------|---------------|
| 01 | 공공행정 | Public Administration | public/ | BRM, ADMCODE, KOOR | 75% |
| 02 | 교육 | Education | - | UNESCO | 59% |
| 03 | 보건의료 | Healthcare | medical/ | MeSH, KCD, ICD11 | 84% |
| 04 | 사회복지 | Social Welfare | - | DATAGOkr | 80% |
| 05 | 법률 | Law | law/ | MOLEG | 55% |
| 06 | 재정금융 | Finance | finance/ | FIBO | 68% |
| 07 | 산업경제 | Industry & Economy | - | KSIC | 57% |
| 08 | 디지털커머스 | Digital Commerce | commerce/ | KSIC | 73% |
| 09 | 문화관광 | Culture & Tourism | - | UNESCO | 62% |
| 10 | 환경기상 | Environment & Weather | - | DATAGOkr, UNESCO | 50% |
| 11 | 과학기술 | Science & Technology | - | OECD-FOS | 83% |
| 12 | 재난안전 | Disaster & Safety | - | DATAGOkr | 48% |

**통계 (v3.5.0):**
- 12개 도메인
- 376개 분류 (72개 중분류, 304개 소분류)
- 221개 용어
- 154개 동의어, 83개 연관관계
- 20개 표준, 255개 표준 레퍼런스 (평균 용어 커버리지 63%)

### 표준 레퍼런스 체계 (v3.2+)

**등록된 표준 (20개):**

*국제 표준 (8개):*
- **STD-SKOS**: W3C SKOS (RDF 기반 지식조직체계)
- **STD-ISO25964**: ISO 25964 (시소러스 표준)
- **STD-DC**: Dublin Core (메타데이터 15개 요소)
- **STD-UNESCO**: UNESCO Thesaurus (7개 도메인, 5개 언어)
- **STD-OECD-FOS**: OECD Fields of Science (6개 대분류, 42개 소분류)
- **STD-FIBO**: FIBO (금융 온톨로지, 10개 도메인, 2,457 클래스)
- **STD-MESH**: MeSH (의학주제어, ~30,000개 항목)
- **STD-ICD11**: ICD-11 (WHO 국제질병분류)

*국내 표준 (6개):*
- **STD-BRM**: 정부기능분류체계 (17개 정책분야, 76개 정책영역)
- **STD-KSIC**: 한국표준산업분류 (11차 개정, 5-level 계층)
- **STD-KCD**: 한국표준질병사인분류 (ICD 기반)
- **STD-MOLEG**: 국가법령정보 (법제처)
- **STD-DATAGOkr**: 공공데이터포털 분류 (16개 분야)
- **STD-STDTERM**: 공공데이터 공통표준용어 (9,027개)

*한국형 응용 표준 (6개):*
- **STD-DCAT-AP-KR**: 한국 공공데이터 메타데이터 표준
- **STD-KOOR**: 한국 기관 온톨로지 (공공기관 표현)
- **STD-ADMCODE**: 행정표준코드 (법정동/행정동)
- **STD-KS-ISO11179**: 메타데이터 레지스트리 표준
- **STD-DBSTD**: 공공기관 DB 표준화 지침
- **STD-DATAQUALITY**: 공공데이터 품질관리 수준평가

**매치 타입 (SKOS 기반):**
- `EXACT_MATCH`: 정확 매칭 (37%)
- `CLOSE_MATCH`: 근접 매칭 (12%)
- `BROAD_MATCH`: 상위 개념 (13%)
- `NARROW_MATCH`: 하위 개념 (26%)
- `RELATED_MATCH`: 연관 개념 (12%)

### 분류 계층 구조 예시

#### 01. 공공행정 (Public Administration) - BRM, ADMCODE 기반
```
C01000001 공공행정 [STD-BRM]
├ C01010001 정부조직·기관관리 [STD-BRM: 정부자원관리]
│ ├ C01010002 공공기관 현황
│ ├ C01010003 정부부처 조직
│ ├ C01010004 산하기관 정보
│ └ C01010005 공공기관 경영정보
├ C01020001 지방행정·자치 [STD-BRM: 지방행정·재정지원]
│ ├ C01020002 행정구역 정보 [STD-ADMCODE]
│ ├ C01020003 지방자치단체
│ ├ C01020004 읍면동 행정기관
│ └ C01020005 지역주민자치
├ C01030001 행정정보화 [STD-BRM: 정보화 기반조성]
│ ├ C01030002 정보자원 현황
│ ├ C01030003 정보시스템
│ └ C01030004 공공데이터 개방 [STD-DCAT-AP-KR]
...
```

#### 03. 보건의료 (Healthcare) - MeSH, KCD, ICD11 기반
```
C03000001 보건의료 [STD-MESH, STD-KCD]
├ C03010001 의료기관 [STD-MESH: D006268 Health Facilities]
│ ├ C03010002 병원·의원 현황 [STD-MESH: D006761 Hospitals]
│ ├ C03010003 약국 현황 [STD-MESH: D010607 Pharmacies]
│ ├ C03010004 의료시설 정보
│ └ C03010005 의료장비 현황
├ C03050001 질병관리
│ ├ C03050002 암·종양 [STD-MESH: D009369, STD-ICD11: 2, STD-KCD: C00-D48]
│ ├ C03050003 안과질환 [STD-KCD: H00-H59]
│ └ C03050004 소화기질환 [STD-KCD: K00-K93]
...
```

#### 06. 재정금융 (Finance) - FIBO 기반
```
C06000001 재정금융 [STD-FIBO]
├ C06010001 통화정책 [STD-FIBO: fibo-fbc-fct-mkt]
│ ├ C06010002 기준금리 [STD-FIBO: fibo-ind-ir-ir/BaseRate]
│ ├ C06010003 통화량
│ └ C06010004 공개시장운영
├ C06040001 자본시장 [STD-FIBO: SEC, DER]
│ ├ C06040002 주식 [STD-FIBO: fibo-sec-eq-eq/Equity]
│ ├ C06040003 채권 [STD-FIBO: fibo-sec-dbt-dbti/Bond]
│ └ C06040004 파생상품 [STD-FIBO: fibo-der-drc-bsc/Derivative]
...
```

*기타 도메인의 상세 구조는 context.txt 참조*

### 데이터베이스 스키마

**MC_CLSF (분류)**
```sql
CLSF_ID     VARCHAR2(32)   -- 분류 ID (예: C01010001)
CLSF_NAME   VARCHAR2(500)  -- 분류명
CLSF_DESC   VARCHAR2(4000) -- 분류 설명
PRT_CLSF_ID VARCHAR2(32)   -- 상위 분류 ID
GROUP_YN    CHAR(1)        -- 그룹 여부 (Y: 상위, N: 하위), 기본값 'N'
DELETE_YN   CHAR(1)        -- 삭제 여부, 기본값 'N'
README      CLOB           -- 비고 (상세 설명)
```
- 최상위 `PRT_CLSF_ID`: `03facd74b2d24f7cab807b8980391649`

**MC_TERM (용어)**
```sql
TERM_ID      VARCHAR2(32)   -- 용어 ID (예: T01010001)
TERM_NAME    VARCHAR2(500)  -- 용어명 (한글)
TERM_NAME_EN VARCHAR2(500)  -- 영문명
ACRONYM      VARCHAR2(100)  -- 약어 (예: OMO, D2C, AI)
TERM_DESC    VARCHAR2(4000) -- 용어 설명
DIC_ID       VARCHAR2(32)   -- 사전 ID (루트: 4147179070a84d3887b97eb57085d850)
TERM_TYPE    CHAR(1)        -- 용어 유형 (T: 일반 용어), 기본값 'T'
DELETE_YN    CHAR(1)        -- 삭제 여부, 기본값 'N'
README       CLOB           -- 연결 분류 ID (예: C01010001)
```

**MC_TERM_REL (용어 관계)**
```sql
TERM_ID     VARCHAR2(32)   -- 용어 ID
REL_TYPE    CHAR(1)        -- 관계 유형 ('S': 동의어, 'T': 연관/계층)
REL_TERM_ID VARCHAR2(32)   -- 관계 대상 (동의어 텍스트 또는 용어 ID)
```
- 동의어(S): 154개
- 연관 용어 및 계층(T): 83개

**MC_STANDARD (표준 레지스트리)** ← v3.2+
```sql
STD_ID       VARCHAR2(32)   -- 표준 ID (예: STD-MESH)
STD_CODE     VARCHAR2(100)  -- 표준 코드 (예: MeSH)
STD_NAME_KO  VARCHAR2(500)  -- 한글명
STD_NAME_EN  VARCHAR2(500)  -- 영문명
STD_TYPE     VARCHAR2(50)   -- 유형 (INTERNATIONAL|NATIONAL|DOMAIN)
STD_SCOPE    VARCHAR2(50)   -- 범위 (ONTOLOGY|CLASSIFICATION|TERMINOLOGY|METADATA)
ORGANIZATION VARCHAR2(500)  -- 관리 기관
VERSION      VARCHAR2(100)  -- 버전
URI          VARCHAR2(1000) -- 참조 URI
STD_DESC     CLOB           -- 설명
```

**MC_CLSF_STD_REF (분류 표준 레퍼런스)** ← v3.2+
```sql
CLSF_ID       VARCHAR2(32)   -- 분류 ID
STD_ID        VARCHAR2(32)   -- 표준 ID
EXTERNAL_ID   VARCHAR2(500)  -- 해당 표준 내 ID/코드
EXTERNAL_NAME VARCHAR2(500)  -- 해당 표준 내 명칭
MATCH_TYPE    VARCHAR2(50)   -- 매치 타입 (EXACT_MATCH 등)
CONFIDENCE    NUMBER(3,2)    -- 신뢰도 (0.0~1.0)
NOTE          CLOB           -- 비고
```

**MC_TERM_STD_REF (용어 표준 레퍼런스)** ← v3.2+
```sql
TERM_ID       VARCHAR2(32)   -- 용어 ID
STD_ID        VARCHAR2(32)   -- 표준 ID
EXTERNAL_ID   VARCHAR2(500)  -- 해당 표준 내 ID/코드
EXTERNAL_NAME VARCHAR2(500)  -- 해당 표준 내 명칭
MATCH_TYPE    VARCHAR2(50)   -- 매치 타입
CONFIDENCE    NUMBER(3,2)    -- 신뢰도
NOTE          CLOB           -- 비고
```

### 그래프 데이터베이스 (Memgraph)

**노드 타입:**
- `:Classification` - 분류 노드 (376개)
- `:Term` - 용어 노드 (221개)
- `:Synonym` - 동의어 노드 (154개)
- `:Standard` - 표준 노드 (20개) ← v3.2+

**관계 타입:**
- `:PARENT_OF` - 계층 관계 (분류↔분류, 용어↔용어)
- `:BELONGS_TO` - 용어가 분류에 속함
- `:SYNONYM_OF` - 용어의 동의어
- `:RELATED_TO` - 용어 간 연관 관계
- `:MAPPED_TO` - 표준 매핑 관계 ← v3.2+

**노드 속성:**
- `display_name` - 모든 노드에 `이름 (:라벨)` 형식으로 표시
  - 예: `'공공행정 (:Classification)'`, `'암 (:Term)'`, `'MeSH (:Standard)'`

## 작업 가이드 (v3.6)

### 분류/용어 추가 또는 수정

1. **ontology.json 직접 편집**
   - JSON 편집기 사용 권장 (VSCode, Sublime Text 등)
   - ID 체계 준수:
     - 분류: `C + DD(도메인) + LL(중분류) + SSSS(일련번호)` (예: C01010001)
     - 용어: `T + DD(도메인) + LL(중분류) + SSSS(일련번호)` (예: T01010001)

2. **재생성 및 검증**
   ```bash
   python3 generate.py          # 모든 출력 파일 생성
   python3 validate_ontology.py # 검증 (0 errors, 0 warnings)
   ```

### ontology.json 구조 예시

```json
{
  "metadata": {
    "version": "3.6.0",
    "last_updated": "2025-12-10",
    "description": "MC 분류·용어 통합 체계 (단일 마스터 파일)"
  },
  "standards": {
    "count": 20,
    "registry": [...]
  },
  "domains": [
    {
      "code": "01",
      "name_ko": "공공행정",
      "name_en": "Public Administration",
      "primary_standards": ["STD-BRM", "STD-DATAGOkr"],
      "classifications": [
        {
          "id": "C01010001",
          "name": "정부조직·기관관리",
          "description": "정부조직·기관관리를 다루는 분류",
          "readme": "중앙행정기관, 지방자치단체, 공공기관 등",
          "group": false,
          "level": 1,
          "parent_id": "C01000001",
          "standard_refs": [
            {
              "standard_id": "STD-BRM",
              "external_id": "정부자원관리",
              "match_type": "RELATED_MATCH",
              "confidence": 0.8
            }
          ],
          "children": [...]
        }
      ],
      "terms": [
        {
          "id": "T01010001",
          "name_ko": "정부조직",
          "name_en": "Government Organization",
          "acronym": null,
          "description": "국가를 운영하는 행정 조직",
          "synonyms": ["행정조직", "정부기구"],
          "related_terms": ["T01010002"],
          "linked_clsf_id": "C01010001",
          "parent_id": null,
          "standard_refs": [
            {
              "standard_id": "STD-DATAGOkr",
              "external_id": "정부조직",
              "match_type": "EXACT_MATCH",
              "confidence": 0.95
            }
          ],
          "children": []
        }
      ]
    }
  ]
}
```

### 표준 레퍼런스 매치 타입

- **EXACT_MATCH** - 정확한 일치 (개념 동일)
- **CLOSE_MATCH** - 밀접한 일치 (개념 유사)
- **BROAD_MATCH** - 상위 개념
- **NARROW_MATCH** - 하위 개념
- **RELATED_MATCH** - 연관 개념
- **DERIVED_FROM** - 파생

### 파일 정책 (v3.6)

**직접 편집:**
- `ontology.json` - **마스터 파일 (유일한 편집 대상)**

**자동 생성 (편집 금지):**
- `generated/` - 모든 생성 파일
  - ontology.txt, ontology.sql, ontology.cypher
  - mc_*_generated.sql (4개)
  - standards_registry.json

**Archive:**
- `archive/` - 구버전 파일 (context.txt, enhanced_data.py, standards_registry.py 등)

### 검증

구조적 정합성 검증 (10개 항목):
```bash
python3 validate_ontology.py
```

검증 항목:
1. JSON-SQL-TXT 3-way 개수 일치
2. ID 유일성 (분류, 용어)
3. ID 일치 (JSON-SQL-TXT)
4. 부모 ID 유효성
5. 필드 값 일치 (이름, 설명 등)
6. ID 형식 (정규식 검증)
7. 용어-분류 연결 (linked_clsf_id)
8. 순환 참조 검사
9. 필수 필드 값 (누락 검사)
10. **표준 레퍼런스** (standard_id, match_type, confidence 검증) ← v3.2+

## 참고 문서

**체계 설계:**
- `CLASSIFICATION_RESTRUCTURE_PLAN.md` - 분류체계 재구축 계획 (v3.0)
- `CLASSIFICATION_EXPANSION_PLAN.md` - 분류 확장 계획 (10→12 도메인)
- `context_schema.md` - context.json 스키마 상세 설명

**표준 분석:**
- `domain_mapping.md` - data.go.kr 기반 도메인 재구성
- `datagoKr_classification_analysis.md` - 실제 데이터셋 분석 결과

**기술 문서:**
- `README_memgraph.md` - Memgraph 그래프 DB 사용법
- `standards_registry.py` - 표준 레지스트리 (20개 표준 정의)

## 버전 이력

- **v1.0** (2024-11-30): 초기 버전 (7개 도메인, 90개 분류)
- **v2.0** (2025-12-01): data.go.kr 기반 도메인 재구성 (10개 도메인)
- **v2.1** (2025-12-01): 실제 데이터셋 기반 세부 분류 확장 (175개 분류)
- **v3.0.0** (2025-12-10): 12개 도메인, 376개 분류, README 100% 커버리지
- **v3.1.0** (2025-12-10): 용어 확장 (124→221개, +78%)
- **v3.2.0** (2025-12-10): 표준 레퍼런스 구현 (20개 표준, 59개 매핑)
- **v3.3.0** (2025-12-10): 표준 레퍼런스 확장 (123개 매핑, 24% 분류 커버리지)
- **v3.4.0** (2025-12-10): 용어 표준 매핑 확장 (74개 용어, 34% 커버리지)
- **v3.5.0** (2025-12-10): 용어 표준 레퍼런스 완성 (140개 용어, 63% 커버리지, 255개 총 매핑)
- **v3.6** (2025-12-10): **단일 마스터 구조** (ontology.json), 파일 정리, 명명 일관성
- **v3.7** (2025-12-10): **분류 표준 레퍼런스 확장** (23.9% → 54.0%, +113개 매핑, 목표 초과 달성)

## 주요 성과 (v2.1 → v3.7)

- **분류:** 175 → 376개 (+115%)
- **용어:** 124 → 221개 (+78%)
- **도메인:** 10 → 12개 (디지털커머스, 과학기술 추가)
- **표준 등록:** 0 → 20개 (국제 8 + 국내 6 + 한국형 6)
- **표준 레퍼런스:** 0 → 368개
  - **분류 매핑: 90/376 (24%) → 203/376 (54%)** ⬆️
  - 용어 매핑: 140/221 (63.3%)
- **분류 설명:** 26% → 100% 커버리지
- **검증 체계:** 6개 → 10개 항목 (표준 레퍼런스 포함)

## 다음 단계 (권장)

1. ~~**분류 표준 레퍼런스 확장**: 24% → 50%+~~ ✅ 완료 (v3.7: 54%)
2. **디지털커머스·과학기술 도메인 표준 매핑**: 27% → 50%+ (e-commerce, scientific taxonomy)
3. **SKOS RDF 출력 구현**: 국제 표준 호환 (RDF/Turtle/JSON-LD)
4. **동의어 확장**: 154 → 250개 (검색 성능 향상)
5. **공통표준용어 자동 매핑**: 9,027개 표준용어 연계
