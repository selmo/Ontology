#!/usr/bin/env python3
"""
기존 enhanced_data.py의 데이터를 새로운 ID 체계로 마이그레이션
"""

import json
from id_mapping import map_classification_id, map_term_id, DOMAIN_MAPPING

# 기존 데이터 로드
with open('backup_20251201/enhanced_data.py', 'r', encoding='utf-8') as f:
    exec(f.read())

# 기존 context.json 로드
with open('backup_20251201/context.json', 'r', encoding='utf-8') as f:
    old_data = json.load(f)

# 새로운 CLASSIFICATION_README 생성
new_classification_readme = {}
for old_id, readme in CLASSIFICATION_README.items():
    new_id = map_classification_id(old_id)
    new_classification_readme[new_id] = readme

# 새로운 TERM_DESCRIPTIONS 생성
new_term_descriptions = {}
for old_id, desc in TERM_DESCRIPTIONS.items():
    new_id = map_term_id(old_id)
    new_term_descriptions[new_id] = desc

# 새로운 TERM_SYNONYMS 생성
new_term_synonyms = {}
for old_id, synonyms in TERM_SYNONYMS.items():
    new_id = map_term_id(old_id)
    new_term_synonyms[new_id] = synonyms

# 새로운 TERM_RELATED 생성 (참조도 업데이트)
new_term_related = {}
for old_id, related_list in TERM_RELATED.items():
    new_id = map_term_id(old_id)
    new_related_list = [map_term_id(r) for r in related_list]
    new_term_related[new_id] = new_related_list

# 새로운 TERM_HIERARCHY 생성 (부모/자식 ID 모두 업데이트)
new_term_hierarchy = {}
for old_child_id, old_parent_id in TERM_HIERARCHY.items():
    new_child_id = map_term_id(old_child_id)
    new_parent_id = map_term_id(old_parent_id)
    new_term_hierarchy[new_child_id] = new_parent_id

# 출력
print("=== 마이그레이션 결과 ===")
print(f"분류 README: {len(CLASSIFICATION_README)} → {len(new_classification_readme)}")
print(f"용어 설명: {len(TERM_DESCRIPTIONS)} → {len(new_term_descriptions)}")
print(f"용어 동의어: {len(TERM_SYNONYMS)} → {len(new_term_synonyms)}")
print(f"용어 연관: {len(TERM_RELATED)} → {len(new_term_related)}")
print(f"용어 계층: {len(TERM_HIERARCHY)} → {len(new_term_hierarchy)}")

print("\n=== 분류 ID 매핑 샘플 ===")
for old_id in list(CLASSIFICATION_README.keys())[:5]:
    new_id = map_classification_id(old_id)
    print(f"{old_id} → {new_id}")

print("\n=== 용어 ID 매핑 샘플 ===")
for old_id in list(TERM_DESCRIPTIONS.keys())[:5]:
    new_id = map_term_id(old_id)
    print(f"{old_id} → {new_id}")

# enhanced_data_new.py 파일 생성
output_lines = []
output_lines.append('#!/usr/bin/env python3')
output_lines.append('"""')
output_lines.append('분류 및 용어 상세 정보 (data.go.kr 기반 재구성)')
output_lines.append('"""')
output_lines.append('')
output_lines.append('# 분류별 상세 설명 (README)')
output_lines.append('CLASSIFICATION_README = {')
for new_id, readme in sorted(new_classification_readme.items()):
    readme_escaped = readme.replace("'", "\\'")
    output_lines.append(f"    '{new_id}': '{readme_escaped}',")
output_lines.append('}')
output_lines.append('')
output_lines.append('# 용어별 상세 설명 (TERM_DESC)')
output_lines.append('TERM_DESCRIPTIONS = {')
for new_id, desc in sorted(new_term_descriptions.items()):
    desc_escaped = desc.replace("'", "\\'")
    output_lines.append(f"    '{new_id}': '{desc_escaped}',")
output_lines.append('}')
output_lines.append('')
output_lines.append('# 용어별 동의어')
output_lines.append('TERM_SYNONYMS = {')
for new_id, synonyms in sorted(new_term_synonyms.items()):
    output_lines.append(f"    '{new_id}': {synonyms},")
output_lines.append('}')
output_lines.append('')
output_lines.append('# 용어 간 연관 관계')
output_lines.append('TERM_RELATED = {')
for new_id, related in sorted(new_term_related.items()):
    output_lines.append(f"    '{new_id}': {related},")
output_lines.append('}')
output_lines.append('')
output_lines.append('# 용어 계층 구조 (자식 → 부모)')
output_lines.append('TERM_HIERARCHY = {')
for new_child_id, new_parent_id in sorted(new_term_hierarchy.items()):
    output_lines.append(f"    '{new_child_id}': '{new_parent_id}',")
output_lines.append('}')

with open('enhanced_data_new.py', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print("\n✓ enhanced_data_new.py 생성 완료")
