# Paw POS

Initial Python scaffold for an offline-first POS MVP.

Planning and specification support for this project is derived from the [BMAD method](https://github.com/bmad-code-org/bmad-builder) and refined in this repository.
Codex is the primary AI coding assistant; final technical decisions and code acceptance are made by the project owner.

## Included MVP Core
- Basic checkout domain flow (cash-only)
- Inventory list/update operations
- Earnings summaries (daily/weekly/monthly)
- CSV export utilities

## Quick Start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python3 -m paw_pos.cli init-db --db ./paw_pos.sqlite3
python3 -m paw_pos.cli list-products --db ./paw_pos.sqlite3
python3 -m unittest discover -s tests -v
```

## Project Docs

- Scaffold spec (completed bootstrap scope): `docs/specs/story-1-1-bootstrap-scaffold.md`
- Backlog and story tracker: `docs/paw-pos-mvp-backlog.md`
