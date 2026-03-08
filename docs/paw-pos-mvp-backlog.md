# Paw POS MVP Backlog

This is the source of truth for planned and in-progress work.

Provenance: Derived from BMAD planning artifacts, then maintained in-repo.

## Status Legend

- `Done`: implemented and validated
- `In Progress`: currently being implemented
- `Planned`: agreed but not started
- `Blocked`: waiting on a dependency or decision

## Story Workflow

1. Pick a story from this backlog.
2. Create/update its spec in `docs/specs/story-<epic>-<story>-<short-name>.md`.
3. Pair-program implementation in small steps.
4. Run tests.
5. Update story status and notes here.

## Epic 1: Backend MVP Completion

### Story 1.1 - Bootstrap Scaffold
- Status: Done
- Spec: `docs/specs/story-1-1-bootstrap-scaffold.md`
- Notes: Initial Python package, SQLite schema, service layer, CSV exporters, baseline tests.

### Story 1.2 - Product Management Commands
- Status: Planned
- Spec: `docs/specs/story-1-2-product-management.md` (create when starting)
- Scope:
  - Add product command
  - Adjust stock command
  - Product list output polish

### Story 1.3 - Checkout Command Flow
- Status: Planned
- Spec: `docs/specs/story-1-3-checkout-flow.md` (create when starting)
- Scope:
  - Record sale command
  - Catalog and manual line support
  - Cash received and change output
  - Validation and clear error messages

### Story 1.4 - Earnings Commands
- Status: Planned
- Spec: `docs/specs/story-1-4-earnings.md` (create when starting)
- Scope:
  - Daily summary command
  - Weekly summary command
  - Monthly summary command

### Story 1.5 - CSV Backup and Restore
- Status: Planned
- Spec: `docs/specs/story-1-5-backup-restore.md` (create when starting)
- Scope:
  - Export products and sales
  - Restore/import flow with safety prompts

### Story 1.6 - Test Expansion and Hardening
- Status: Planned
- Spec: `docs/specs/story-1-6-test-hardening.md` (create when starting)
- Scope:
  - Manual-line sale tests
  - Out-of-stock tests
  - Weekly/monthly boundary tests
  - CSV coverage tests

## Epic 2: Operator-Focused UI

### Story 2.1 - UI Shell and Navigation
- Status: Planned
- Spec: `docs/specs/story-2-1-ui-shell.md` (create when starting)

### Story 2.2 - Checkout Screen
- Status: Planned
- Spec: `docs/specs/story-2-2-checkout-screen.md` (create when starting)

### Story 2.3 - Inventory Screen
- Status: Planned
- Spec: `docs/specs/story-2-3-inventory-screen.md` (create when starting)

### Story 2.4 - Earnings Screen
- Status: Planned
- Spec: `docs/specs/story-2-4-earnings-screen.md` (create when starting)

## Epic 3: Pilot Readiness

### Story 3.1 - Soft Launch Checklist
- Status: Planned
- Spec: `docs/specs/story-3-1-soft-launch.md` (create when starting)

### Story 3.2 - Pilot Fixes and Stability
- Status: Planned
- Spec: create after pilot findings are collected
