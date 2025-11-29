# Repository Guidelines

## Project Structure & Module Organization
- `commerce`, `finance`, `law`, `medical`, `public`: domain PDFs/HWP/HWPX. Place new files in the correct domain with descriptive, dated names.
- `ontology/`: taxonomy context (`context.txt`, `context.xlsx`) and schema SQL (`mc_clsf.sql`, `mc_term.sql`). Update here when adding or adjusting classifications/terms.
- `migration.py`: helper for extracting preview text from HWP/HWPX files via `hwp5proc`; keep it small and dependency-light.
- `CLAUDE.md` and `.claude/`: agent prompt/configuration; change only when updating guidance.

## Build, Test, and Development Commands
- `python migration.py public/<file.hwpx>`: dump preview text for quick review or migration (requires `hwp5proc`/pyhwp in PATH).
- `python -m compileall migration.py`: fast syntax check after edits to the helper script.
- `rg "<keyword>" ontology`: search taxonomy terms or IDs.

## Coding Style & Naming Conventions
- Python: follow PEP 8, 4-space indents, guard subprocess calls, and return clear error messages (see `migration.py`).
- Filenames: use ASCII where possible and include date/topic, e.g., `2024_finance_liquidity-risk.pdf`; avoid whitespace-heavy names to simplify scripting.
- Taxonomy IDs: maintain the `C`/`T` prefixes and numbering described in `ontology/context.txt`; keep SQL files aligned if schemas change.

## Testing Guidelines
- No automated suite; smoke-test changes by running `python migration.py <sample.hwp>` and confirming readable output.
- When adding taxonomy entries, validate references with `rg` to ensure IDs and labels match existing usage.
- For large binaries, open locally to confirm the file is intact and uncorrupted before committing.

## Ontology Maintenance (context.txt, mc_*.sql)
- `ontology/context.txt` is the source; mirror its order into `mc_clsf.sql`/`mc_term.sql` (see `CLAUDE.md` for ID/root IDs).
- Enforce `C/T + DD + LL + SSSS`; terms reuse parent `LL`; set `GROUP_YN='Y'` only when children exist; store mapped CLSF ID in `README`; omit defaulted columns and keep spacing consistent. Ignore `context.xlsx` (deprecated).
- Before commit: `rg "C0" ontology/context.txt` to catch gaps/dupes, then scan new INSERT blocks for parent IDs and README links.
- Graph export: `python ontology/generate_cypher.py > ontology/mc_graph.cypher` regenerates Cypher with `display_name` set to `"name (Class|Term)"` and merges semantic edges from `ontology/additional_relation.txt` (tab-separated; one relation per line).

## Commit & Pull Request Guidelines
- Commit messages: short, imperative summaries (≤72 chars), e.g., `add 2024 finance liquidity brief`.
- PRs: enumerate added files by domain, note source/public status, describe taxonomy or script changes, and include any manual checks performed (e.g., `migration.py` output verified).

## Security & Data Handling
- Only commit documents that are publicly shareable; avoid sensitive or licensed material without approval.
- Do not store secrets or credentials; environment-specific settings should live outside the repo.
- Keep binaries versioned only when necessary; prefer links if licensing is unclear.
