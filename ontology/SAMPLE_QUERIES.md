# 샘플 쿼리 모음

**버전:** 3.11.0
**최종 업데이트:** 2025-12-11

이 문서는 ontology.json 데이터를 활용하는 Cypher 및 SQL 쿼리 예시를 제공합니다.

---

## Cypher 쿼리 (Memgraph/Neo4j)

### 기본 조회

#### 1. 모든 도메인 분류 조회
```cypher
MATCH (c:Classification)
WHERE c.level = 0
RETURN c.id AS domain_id, c.name AS domain_name
ORDER BY c.id;
```

#### 2. 특정 도메인의 전체 분류 계층 조회
```cypher
MATCH path = (root:Classification {id: 'C01000001'})-[:PARENT_OF*]->(child:Classification)
RETURN path
LIMIT 50;
```

#### 3. 특정 분류의 직속 하위 분류 조회
```cypher
MATCH (parent:Classification {id: 'C01000001'})-[:PARENT_OF]->(child:Classification)
RETURN child.id AS id, child.name AS name, child.level AS level
ORDER BY child.id;
```

### SYNONYM 관계 조회 (v3.11 하이브리드 구조)

#### 4. Term → Term SYNONYM_OF 조회
```cypher
MATCH (t1:Term)-[:SYNONYM_OF]->(t2:Term)
WHERE t1.id < t2.id  // 양방향 중복 제거
RETURN t1.id AS term1_id, t1.name_ko AS term1,
       t2.id AS term2_id, t2.name_ko AS term2;
```

#### 5. 특정 용어의 모든 동의어 조회 (문자열 + Term)
```cypher
MATCH (t:Term {id: 'T03010001'})
OPTIONAL MATCH (t)-[:SYNONYM_OF]->(syn_term:Term)
OPTIONAL MATCH (t)-[:SYNONYM_OF]->(syn_node:Synonym)
RETURN t.name_ko AS term,
       collect(DISTINCT syn_term.name_ko) AS synonym_terms,
       collect(DISTINCT syn_node.value) AS synonym_strings;
```

#### 6. 동의어를 가진 모든 용어 조회
```cypher
MATCH (t:Term)-[:SYNONYM_OF]->(s)
RETURN t.id AS term_id, t.name_ko AS term,
       collect(CASE
         WHEN s:Term THEN s.name_ko
         WHEN s:Synonym THEN s.value
       END) AS synonyms
ORDER BY t.id;
```

### RELATED_TO 관계 조회

#### 7. 연관 용어 네트워크 조회
```cypher
MATCH (t1:Term)-[:RELATED_TO]->(t2:Term)
WHERE t1.id < t2.id  // 양방향 중복 제거
RETURN t1.id AS term1_id, t1.name_ko AS term1,
       t2.id AS term2_id, t2.name_ko AS term2;
```

#### 8. 특정 용어의 연관 용어 조회
```cypher
MATCH (t:Term {name_ko: '의료기관'})-[:RELATED_TO]->(related:Term)
RETURN t.name_ko AS term,
       collect(related.name_ko) AS related_terms;
```

#### 9. 연관 용어가 많은 허브 용어 Top 10
```cypher
MATCH (t:Term)-[:RELATED_TO]->(related:Term)
WITH t, count(related) AS connection_count
WHERE connection_count > 0
RETURN t.id AS term_id, t.name_ko AS term, connection_count
ORDER BY connection_count DESC
LIMIT 10;
```

### SIMILAR_TO 관계 조회

#### 10. 유사 분류 조회
```cypher
MATCH (c1:Classification)-[:SIMILAR_TO]->(c2:Classification)
WHERE c1.id < c2.id  // 양방향 중복 제거
RETURN c1.id AS clsf1_id, c1.name AS clsf1,
       c2.id AS clsf2_id, c2.name AS clsf2;
```

#### 11. 도메인 간 유사 분류 네트워크
```cypher
MATCH (c1:Classification)-[:SIMILAR_TO]->(c2:Classification)
WHERE substring(c1.id, 1, 3) <> substring(c2.id, 1, 3)  // 다른 도메인
AND c1.id < c2.id
RETURN c1.id, c1.name, c2.id, c2.name;
```

### 복합 쿼리

#### 12. 특정 용어의 모든 관계 조회
```cypher
MATCH (t:Term {name_ko: '국가예산'})
OPTIONAL MATCH (t)-[:BELONGS_TO]->(c:Classification)
OPTIONAL MATCH (t)-[:SYNONYM_OF]->(s)
OPTIONAL MATCH (t)-[:RELATED_TO]->(r:Term)
RETURN t.name_ko AS term,
       c.name AS classification,
       collect(DISTINCT CASE
         WHEN s:Term THEN s.name_ko
         WHEN s:Synonym THEN s.value
       END) AS synonyms,
       collect(DISTINCT r.name_ko) AS related_terms;
```

#### 13. 특정 분류의 모든 용어와 동의어 조회
```cypher
MATCH (c:Classification {id: 'C03010001'})<-[:BELONGS_TO]-(t:Term)
OPTIONAL MATCH (t)-[:SYNONYM_OF]->(s)
RETURN t.id AS term_id, t.name_ko AS term,
       collect(DISTINCT CASE
         WHEN s:Term THEN s.name_ko
         WHEN s:Synonym THEN s.value
       END) AS synonyms
ORDER BY t.id;
```

#### 14. 표준 레퍼런스가 있는 분류 조회
```cypher
MATCH (c:Classification)
WHERE exists(c.standard_refs) AND size(c.standard_refs) > 0
RETURN c.id AS id, c.name AS name,
       c.standard_refs AS standards
ORDER BY c.id;
```

#### 15. 특정 표준을 참조하는 모든 분류/용어 조회
```cypher
MATCH (c:Classification)
WHERE 'SKOS' IN c.standard_refs
RETURN 'Classification' AS type, c.id AS id, c.name AS name
UNION
MATCH (t:Term)
WHERE 'SKOS' IN t.standard_refs
RETURN 'Term' AS type, t.id AS id, t.name_ko AS name;
```

### 통계 쿼리

#### 16. 노드 및 관계 통계
```cypher
MATCH (c:Classification)
WITH count(c) AS clsf_count
MATCH (t:Term)
WITH clsf_count, count(t) AS term_count
MATCH (s:Synonym)
WITH clsf_count, term_count, count(s) AS synonym_count
MATCH ()-[r:SYNONYM_OF]->()
WITH clsf_count, term_count, synonym_count, count(r) AS synonym_rel_count
MATCH ()-[r2:RELATED_TO]->()
WITH clsf_count, term_count, synonym_count, synonym_rel_count, count(r2) AS related_count
MATCH ()-[r3:SIMILAR_TO]->()
RETURN clsf_count AS classifications,
       term_count AS terms,
       synonym_count AS synonym_nodes,
       synonym_rel_count AS synonym_relationships,
       related_count AS related_relationships,
       count(r3) AS similar_relationships;
```

#### 17. 도메인별 용어 개수
```cypher
MATCH (c:Classification)
WHERE c.level = 0
MATCH (c)-[:PARENT_OF*]->(sub:Classification)<-[:BELONGS_TO]-(t:Term)
RETURN c.id AS domain_id, c.name AS domain, count(DISTINCT t) AS term_count
ORDER BY c.id;
```

#### 18. 동의어가 없는 용어 찾기
```cypher
MATCH (t:Term)
WHERE NOT (t)-[:SYNONYM_OF]->()
RETURN t.id AS term_id, t.name_ko AS term, t.name_en AS term_en
ORDER BY t.id
LIMIT 20;
```

### 검색 쿼리

#### 19. 이름으로 용어 검색 (부분 일치)
```cypher
MATCH (t:Term)
WHERE t.name_ko CONTAINS '의료' OR t.name_en CONTAINS 'medical'
RETURN t.id AS id, t.name_ko AS name_ko, t.name_en AS name_en
ORDER BY t.id;
```

#### 20. 동의어로 용어 검색
```cypher
MATCH (t:Term)-[:SYNONYM_OF]->(s:Synonym)
WHERE s.value CONTAINS '병원'
RETURN t.id AS term_id, t.name_ko AS term, s.value AS matched_synonym;
```

---

## SQL 쿼리 (Oracle/PostgreSQL)

### 기본 조회

#### 1. 모든 도메인 분류 조회
```sql
SELECT CLSF_ID, CLSF_NAME
FROM MC_CLSF
WHERE PRT_CLSF_ID = '03facd74b2d24f7cab807b8980391649'
ORDER BY CLSF_ID;
```

#### 2. 특정 도메인의 모든 분류 조회 (재귀 CTE)
```sql
WITH RECURSIVE clsf_hierarchy AS (
  -- 루트 (도메인)
  SELECT CLSF_ID, CLSF_NAME, PRT_CLSF_ID, 0 AS depth
  FROM MC_CLSF
  WHERE CLSF_ID = 'C01000001'

  UNION ALL

  -- 재귀: 하위 분류
  SELECT c.CLSF_ID, c.CLSF_NAME, c.PRT_CLSF_ID, h.depth + 1
  FROM MC_CLSF c
  INNER JOIN clsf_hierarchy h ON c.PRT_CLSF_ID = h.CLSF_ID
)
SELECT CLSF_ID, CLSF_NAME, depth
FROM clsf_hierarchy
ORDER BY CLSF_ID;
```

#### 3. 특정 분류의 직속 하위 분류 조회
```sql
SELECT CLSF_ID, CLSF_NAME
FROM MC_CLSF
WHERE PRT_CLSF_ID = 'C01000001'
ORDER BY CLSF_ID;
```

### 용어 조회

#### 4. 모든 용어와 소속 분류 조회
```sql
SELECT
  t.TERM_ID,
  t.TERM_NAME,
  t.TERM_NAME_EN,
  c.CLSF_NAME
FROM MC_TERM t
LEFT JOIN MC_CLSF c ON t.README = c.CLSF_ID
ORDER BY t.TERM_ID;
```

#### 5. 특정 분류의 모든 용어 조회
```sql
SELECT TERM_ID, TERM_NAME, TERM_NAME_EN, ACRONYM
FROM MC_TERM
WHERE README = 'C03010001'
ORDER BY TERM_ID;
```

### 동의어 조회

#### 6. Term의 모든 동의어 조회 (문자열 동의어)
```sql
SELECT
  t.TERM_ID,
  t.TERM_NAME,
  r.REL_TERM_ID AS synonym
FROM MC_TERM t
INNER JOIN MC_TERM_REL r ON t.TERM_ID = r.TERM_ID
WHERE r.REL_TYPE = 'S'
  AND t.TERM_ID = 'T01010001'
ORDER BY r.REL_TERM_ID;
```

#### 7. Term → Term 동의어 관계 조회
```sql
SELECT
  t1.TERM_ID AS term1_id,
  t1.TERM_NAME AS term1,
  t2.TERM_ID AS term2_id,
  t2.TERM_NAME AS term2
FROM MC_TERM_REL r
INNER JOIN MC_TERM t1 ON r.TERM_ID = t1.TERM_ID
INNER JOIN MC_TERM t2 ON r.REL_TERM_ID = t2.TERM_ID
WHERE r.REL_TYPE = 'S'
  AND r.TERM_ID < r.REL_TERM_ID  -- 중복 제거
ORDER BY t1.TERM_ID;
```

#### 8. 동의어 개수로 정렬
```sql
SELECT
  t.TERM_ID,
  t.TERM_NAME,
  COUNT(r.REL_TERM_ID) AS synonym_count
FROM MC_TERM t
LEFT JOIN MC_TERM_REL r ON t.TERM_ID = r.TERM_ID AND r.REL_TYPE = 'S'
GROUP BY t.TERM_ID, t.TERM_NAME
HAVING COUNT(r.REL_TERM_ID) > 0
ORDER BY synonym_count DESC, t.TERM_ID
LIMIT 20;
```

### 연관 용어 조회

#### 9. 특정 용어의 연관 용어 조회
```sql
SELECT
  t1.TERM_NAME AS term,
  t2.TERM_NAME AS related_term
FROM MC_TERM_REL r
INNER JOIN MC_TERM t1 ON r.TERM_ID = t1.TERM_ID
INNER JOIN MC_TERM t2 ON r.REL_TERM_ID = t2.TERM_ID
WHERE r.REL_TYPE = 'T'
  AND t1.TERM_ID = 'T03010001'
ORDER BY t2.TERM_NAME;
```

#### 10. 연관 용어가 많은 허브 용어 Top 10
```sql
SELECT
  t.TERM_ID,
  t.TERM_NAME,
  COUNT(r.REL_TERM_ID) AS connection_count
FROM MC_TERM t
INNER JOIN MC_TERM_REL r ON t.TERM_ID = r.TERM_ID
WHERE r.REL_TYPE = 'T'
GROUP BY t.TERM_ID, t.TERM_NAME
ORDER BY connection_count DESC
LIMIT 10;
```

### 복합 쿼리

#### 11. 용어와 모든 관계 정보 조회
```sql
SELECT
  t.TERM_ID,
  t.TERM_NAME,
  t.TERM_NAME_EN,
  c.CLSF_NAME AS classification,
  STRING_AGG(
    CASE WHEN r.REL_TYPE = 'S' THEN r.REL_TERM_ID END,
    ', '
  ) AS synonyms,
  STRING_AGG(
    CASE WHEN r.REL_TYPE = 'T' THEN r.REL_TERM_ID END,
    ', '
  ) AS related_terms
FROM MC_TERM t
LEFT JOIN MC_CLSF c ON t.README = c.CLSF_ID
LEFT JOIN MC_TERM_REL r ON t.TERM_ID = r.TERM_ID
WHERE t.TERM_ID = 'T01040001'
GROUP BY t.TERM_ID, t.TERM_NAME, t.TERM_NAME_EN, c.CLSF_NAME;
```

#### 12. 특정 도메인의 모든 용어와 동의어 개수
```sql
SELECT
  t.TERM_ID,
  t.TERM_NAME,
  COUNT(DISTINCT r.REL_TERM_ID) FILTER (WHERE r.REL_TYPE = 'S') AS synonym_count,
  COUNT(DISTINCT r.REL_TERM_ID) FILTER (WHERE r.REL_TYPE = 'T') AS related_count
FROM MC_TERM t
LEFT JOIN MC_TERM_REL r ON t.TERM_ID = r.TERM_ID
WHERE t.TERM_ID LIKE 'T01%'
GROUP BY t.TERM_ID, t.TERM_NAME
ORDER BY t.TERM_ID;
```

### 검색 쿼리

#### 13. 이름으로 용어 검색 (부분 일치)
```sql
SELECT TERM_ID, TERM_NAME, TERM_NAME_EN
FROM MC_TERM
WHERE TERM_NAME LIKE '%의료%'
   OR TERM_NAME_EN LIKE '%medical%'
ORDER BY TERM_ID;
```

#### 14. 동의어로 용어 검색
```sql
SELECT DISTINCT
  t.TERM_ID,
  t.TERM_NAME,
  r.REL_TERM_ID AS matched_synonym
FROM MC_TERM t
INNER JOIN MC_TERM_REL r ON t.TERM_ID = r.TERM_ID
WHERE r.REL_TYPE = 'S'
  AND r.REL_TERM_ID LIKE '%병원%'
ORDER BY t.TERM_ID;
```

### 통계 쿼리

#### 15. 전체 통계
```sql
SELECT
  (SELECT COUNT(*) FROM MC_CLSF) AS classification_count,
  (SELECT COUNT(*) FROM MC_TERM) AS term_count,
  (SELECT COUNT(*) FROM MC_TERM_REL WHERE REL_TYPE = 'S') AS synonym_count,
  (SELECT COUNT(*) FROM MC_TERM_REL WHERE REL_TYPE = 'T') AS related_count;
```

#### 16. 도메인별 분류 및 용어 개수
```sql
WITH domain_clsf AS (
  SELECT CLSF_ID, CLSF_NAME
  FROM MC_CLSF
  WHERE PRT_CLSF_ID = '03facd74b2d24f7cab807b8980391649'
)
SELECT
  d.CLSF_ID AS domain_id,
  d.CLSF_NAME AS domain_name,
  COUNT(DISTINCT c.CLSF_ID) AS classification_count,
  COUNT(DISTINCT t.TERM_ID) AS term_count
FROM domain_clsf d
LEFT JOIN MC_CLSF c ON c.CLSF_ID LIKE CONCAT(SUBSTRING(d.CLSF_ID, 1, 3), '%')
LEFT JOIN MC_TERM t ON t.TERM_ID LIKE CONCAT(SUBSTRING(d.CLSF_ID, 1, 3), '%')
GROUP BY d.CLSF_ID, d.CLSF_NAME
ORDER BY d.CLSF_ID;
```

#### 17. 동의어가 없는 용어 개수
```sql
SELECT COUNT(*) AS terms_without_synonyms
FROM MC_TERM t
WHERE NOT EXISTS (
  SELECT 1 FROM MC_TERM_REL r
  WHERE r.TERM_ID = t.TERM_ID AND r.REL_TYPE = 'S'
);
```

#### 18. 관계 타입별 통계
```sql
SELECT
  REL_TYPE,
  CASE REL_TYPE
    WHEN 'S' THEN 'Synonym'
    WHEN 'T' THEN 'Related Term'
  END AS relation_type,
  COUNT(*) AS count
FROM MC_TERM_REL
GROUP BY REL_TYPE
ORDER BY REL_TYPE;
```

### 데이터 품질 체크

#### 19. 고아 용어 찾기 (분류 연결 없음)
```sql
SELECT TERM_ID, TERM_NAME
FROM MC_TERM
WHERE README IS NULL OR README NOT IN (SELECT CLSF_ID FROM MC_CLSF)
LIMIT 20;
```

#### 20. 순환 참조 체크 (분류)
```sql
WITH RECURSIVE clsf_path AS (
  SELECT CLSF_ID, PRT_CLSF_ID, ARRAY[CLSF_ID] AS path
  FROM MC_CLSF
  WHERE PRT_CLSF_ID IS NOT NULL

  UNION ALL

  SELECT c.CLSF_ID, c.PRT_CLSF_ID, path || c.CLSF_ID
  FROM MC_CLSF c
  INNER JOIN clsf_path p ON c.PRT_CLSF_ID = p.CLSF_ID
  WHERE NOT c.CLSF_ID = ANY(path)
)
SELECT CLSF_ID, path
FROM clsf_path
WHERE CLSF_ID = ANY(path[2:])
LIMIT 10;
```

---

## 참고

### Cypher vs SQL 차이점

| 기능 | Cypher | SQL |
|------|--------|-----|
| 관계 탐색 | 직관적 (`-[:REL]->`) | JOIN 필요 |
| 재귀 쿼리 | 간단 (`-[:REL*]->`) | CTE 사용 |
| 양방향 관계 | 자동 처리 | 수동 필터링 |
| 그래프 시각화 | 기본 지원 | 별도 도구 필요 |

### 성능 최적화 팁

**Cypher:**
- 인덱스 생성: `CREATE INDEX ON :Term(id)`
- LIMIT 사용으로 대량 결과 제한
- WHERE 절로 필터링 우선

**SQL:**
- 외래 키 인덱스 생성
- JOIN 순서 최적화
- EXPLAIN으로 실행 계획 확인

### 추가 자료

- **README_memgraph.md** - Memgraph 설정 및 사용법
- **context_schema.md** - JSON 스키마 상세 설명
- **term_revision_proposal.md** - v3.11 관계 구조 설계 문서
