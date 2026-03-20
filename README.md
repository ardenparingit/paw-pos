# Paw POS

Paw POS is an offline-first, web-based point-of-sale app for a pet store operator.

The active MVP direction is browser-first: the operator should be able to open Paw POS in a browser, land on a simple home or cockpit view, and move quickly between Sales, Inventory, and Earnings workflows.

Planning and specification support for this project is derived from the [BMAD method](https://github.com/bmad-code-org/BMAD-METHOD) and refined in this repository. Codex is the primary AI coding assistant; final technical decisions and code acceptance are made by the project owner.

## Product Direction

### MVP goal
- Deliver a browser-accessible app shell for daily store operations
- Support core modules for Sales, Inventory, and Earnings
- Stay offline-first so the operator can keep working during connectivity issues
- Preserve room for later cloud sync and API expansion after MVP

## Current Repository Foundation

Today, the repository contains the backend and domain scaffold that the web app will build on:

- SQLite persistence and schema initialization
- Service-layer logic for inventory, sales, and earnings
- CSV export utilities
- Minimal CLI entry points for the current scaffold
- Baseline automated tests for core flows

## Current Scaffold Quick Start

These commands run the existing Python scaffold and tests while the web app is still being built.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
python3 -m paw_pos.cli init-db --db ./paw_pos.sqlite3
python3 -m paw_pos.cli list-products --db ./paw_pos.sqlite3
python3 -m unittest discover -s tests -v
```

## Project Workflow

- Use `docs/paw-pos-mvp-backlog.md` as the source of truth for planned and in-progress work
- Create or update story specs in `docs/specs/` before implementation
- Implement stories in small pair-programming steps
- Run tests and update backlog notes as work progresses

## Project Docs

- Agent instructions: `AGENTS.md`
- Backlog and story tracker: `docs/paw-pos-mvp-backlog.md`
- Web shell baseline story: `docs/specs/story-1-1-web-shell-navigation.md`
- Bootstrap scaffold spec: `docs/specs/story-1-1-bootstrap-scaffold.md`
