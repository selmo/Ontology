import re
from pathlib import Path


ROOT = Path(__file__).parent
ADDITIONAL_REL_PATH = ROOT / "additional_relation.txt"


def _escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace("'", "\\'")


def _extract_clsf_id(readme: str) -> str | None:
    match = re.search(r"C\d{8}", readme)
    return match.group(0) if match else None


def parse_clsf(sql_text: str):
    pattern = re.compile(
        r"VALUES\s*\(\s*'(?P<id>[^']*)'\s*,\s*'(?P<name>[^']*)'\s*,\s*'(?P<desc>[^']*)'\s*,\s*'(?P<parent>[^']*)'\s*,\s*'(?P<group>[YN])'\s*,\s*'(?P<readme>[^']*)'\s*\)",
        re.DOTALL,
    )
    records = []
    for match in pattern.finditer(sql_text):
        item = match.groupdict()
        item["group"] = item["group"] == "Y"
        records.append(item)
    return records


def parse_term(sql_text: str):
    pattern = re.compile(
        r"VALUES\s*\(\s*'(?P<id>[^']*)'\s*,\s*'(?P<name>[^']*)'\s*,\s*'(?P<en>[^']*)'\s*,\s*(?P<acro>NULL|'[^']*')\s*,\s*'(?P<desc>[^']*)'\s*,\s*'(?P<parent>[^']*)'\s*,\s*'(?P<type>[^']*)'\s*,\s*'(?P<readme>[^']*)'\s*\)",
        re.IGNORECASE | re.DOTALL,
    )
    records = []
    for match in pattern.finditer(sql_text):
        item = match.groupdict()
        acro = item["acro"]
        if acro.upper() == "NULL":
            item["acro"] = None
        else:
            item["acro"] = acro.strip("'")
        records.append(item)
    return records


def parse_relations(text: str):
    """
    Expected format per line (tab-separated):
    REL_TYPE  SRC_TERM_ID  DST_TERM_ID  SOURCE_FILE  Note
    Comment lines start with '#'.
    """
    relations = []
    for line in text.splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 5:
            continue
        rel_type, src, dst, source_file, note = [p.strip() for p in parts[:5]]
        if not re.fullmatch(r"[A-Z_]+", rel_type):
            continue
        relations.append(
            {
                "type": rel_type,
                "src": src,
                "dst": dst,
                "source_file": source_file,
                "note": note,
            }
        )
    return relations


def to_cypher(classes, terms, relations):
    lines = [
        "// Auto-generated from mc_clsf.sql and mc_term.sql",
        "CREATE CONSTRAINT class_id IF NOT EXISTS FOR (c:Class) REQUIRE c.id IS UNIQUE;",
        "CREATE CONSTRAINT term_id IF NOT EXISTS FOR (t:Term) REQUIRE t.id IS UNIQUE;",
        "",
    ]
    for clsf in classes:
        cid = _escape(clsf["id"])
        name = _escape(clsf["name"])
        desc = _escape(clsf["desc"])
        readme = _escape(clsf["readme"])
        lines.append(f"MERGE (c:Class {{id:'{cid}'}})")
        lines.append(
            f"SET c.name='{name}', c.display_name='{name} (Class)', c.desc='{desc}', c.readme='{readme}', c.group={str(clsf['group']).lower()};"
        )
        parent = clsf["parent"]
        if parent.startswith("C"):
            pid = _escape(parent)
            lines.append(
                f"MATCH (child:Class {{id:'{cid}'}}),(parent:Class {{id:'{pid}'}}) MERGE (child)-[:CHILD_OF]->(parent);"
            )
        lines.append("")
    for term in terms:
        tid = _escape(term["id"])
        name = _escape(term["name"])
        en = _escape(term["en"])
        desc = _escape(term["desc"])
        readme = _escape(term["readme"])
        lines.append(f"MERGE (t:Term {{id:'{tid}'}})")
        set_parts = [
            f"t.name='{name}'",
            f"t.display_name='{name} (Term)'",
            f"t.desc='{desc}'",
            f"t.readme='{readme}'",
            f"t.type='{_escape(term['type'])}'",
        ]
        if en:
            set_parts.append(f"t.en='{en}'")
        if term["acro"]:
            set_parts.append(f"t.acronym='{_escape(term['acro'])}'")
        lines.append("SET " + ", ".join(set_parts) + ";")
        parent_term = term["parent"]
        if parent_term.startswith("T"):
            pid = _escape(parent_term)
            lines.append(
                f"MATCH (child:Term {{id:'{tid}'}}),(parent:Term {{id:'{pid}'}}) MERGE (child)-[:TERM_CHILD_OF]->(parent);"
            )
        belongs = _extract_clsf_id(term["readme"])
        if belongs:
            cid = _escape(belongs)
            lines.append(
                f"MATCH (term:Term {{id:'{tid}'}}),(clsf:Class {{id:'{cid}'}}) MERGE (term)-[:BELONGS_TO]->(clsf);"
            )
        lines.append("")
    for rel in relations:
        src = _escape(rel["src"])
        dst = _escape(rel["dst"])
        rtype = rel["type"]
        source_file = _escape(rel["source_file"])
        note = _escape(rel["note"])
        lines.append(
            f"MATCH (s:Term {{id:'{src}'}}),(d:Term {{id:'{dst}'}}) "
            f"MERGE (s)-[r:{rtype}]->(d) "
            f"SET r.source_file='{source_file}', r.note='{note}';"
        )
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def main():
    clsf_sql = (ROOT / "mc_clsf.sql").read_text()
    term_sql = (ROOT / "mc_term.sql").read_text()
    additional_relations = []
    if ADDITIONAL_REL_PATH.exists():
        additional_relations = parse_relations(ADDITIONAL_REL_PATH.read_text())
    classes = parse_clsf(clsf_sql)
    terms = parse_term(term_sql)
    cypher = to_cypher(classes, terms, additional_relations)
    print(cypher)


if __name__ == "__main__":
    main()
