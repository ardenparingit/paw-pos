# Paw POS Bootstrap Scaffold Spec

Status: Completed (scaffold only)

This document is intentionally scoped to the initial backend scaffold. It is not the full MVP delivery plan.

Provenance: Derived from BMAD workflow artifacts (brainstorming + quick-spec) and then refined in-repo for project clarity.

## Overview

### Problem Statement
The pet store currently runs checkout, inventory tracking, and earnings tracking manually in notebooks. This is slow, unstructured, and error-prone for a single non-technical operator.

### Solution
Create an offline-first Python scaffold for Paw POS with SQLite schema, service-layer business logic, CSV exporters, minimal CLI wiring, and baseline tests.

### Scope (Scaffold Scope)

In Scope:
- Python package setup and project metadata
- SQLite persistence schema and initialization
- Core domain models and service classes
- CSV export helpers
- Minimal CLI entry and app facade
- Baseline automated tests for core flows

Out of Scope:
- Full productized CLI/API command set
- Production-grade error and backup flows
- Mobile/UI implementation
- Full MVP feature-complete delivery

## Technical Direction

### Architecture Decision
- Project structure: Python package with service-layer modules
- Data layer: SQLite (local file)
- Runtime mode: offline-first, no backend service required for MVP
- Python strategy: strategic use for core domain/services and exports

### Key Technical Decisions
- Checkout domain supports catalog and manual sale lines
- Stock auto-deducts on successful sale persistence
- Earnings service supports daily/weekly/monthly summaries
- Currency stored in integer cents
- SQLite foreign keys enabled

## Context for Development

### Codebase Patterns
- Clean-slate repo (no legacy constraints)
- Layered structure:
  - `db.py` for schema and persistence utilities
  - `services/` for business logic
  - `exporters/` for CSV output
  - `app.py` as application facade
- Standard library-first scaffold to minimize setup friction

### Files to Reference

| File | Purpose |
| ---- | ------- |
| `src/paw_pos/db.py` | DB connection and schema initialization |
| `src/paw_pos/models.py` | Domain dataclasses and data contracts |
| `src/paw_pos/services/inventory.py` | Inventory operations |
| `src/paw_pos/services/sales.py` | Checkout and stock deduction logic |
| `src/paw_pos/services/earnings.py` | Earnings aggregation logic |
| `src/paw_pos/exporters/csv_export.py` | CSV export capability |
| `src/paw_pos/app.py` | Unified app facade |
| `tests/test_sales_flow.py` | Functional flow tests |

### Technical Decisions
- Currency stored as integer cents to avoid floating-point errors
- SQLite foreign keys enabled
- Service methods validate business rules (cash-only, no discount path)

## Implementation Plan (Scaffold)

### Tasks
- [x] Task 1: Initialize Python project structure and package metadata
  - File: `pyproject.toml`, `README.md`, `.gitignore`
  - Action: Define project metadata and local development instructions
  - Notes: Keep dependency-light scaffold

- [x] Task 2: Create persistence foundation
  - File: `src/paw_pos/db.py`
  - Action: Add SQLite connection helper and schema initializer for products, sales, and sale_items
  - Notes: Ensure foreign keys are enabled and schema is idempotent

- [x] Task 3: Define domain contracts
  - File: `src/paw_pos/models.py`
  - Action: Add dataclasses for sale lines, sale results, and summary records
  - Notes: Model both catalog and manual sale lines

- [x] Task 4: Implement inventory service
  - File: `src/paw_pos/services/inventory.py`
  - Action: Add product upsert, list, and stock adjustment operations
  - Notes: Keep API friendly for non-technical operator workflow

- [x] Task 5: Implement sales service
  - File: `src/paw_pos/services/sales.py`
  - Action: Add cash checkout workflow with stock deduction and change calculation
  - Notes: Reject insufficient cash and out-of-stock cases

- [x] Task 6: Implement earnings service
  - File: `src/paw_pos/services/earnings.py`
  - Action: Add daily/weekly/monthly summary queries
  - Notes: Use SQL date bucketing with explicit period handling

- [x] Task 7: Implement CSV exports
  - File: `src/paw_pos/exporters/csv_export.py`
  - Action: Add export methods for products and sales
  - Notes: Produce portable CSV files for backup/reporting

- [x] Task 8: Add app facade and CLI entry
  - File: `src/paw_pos/app.py`, `src/paw_pos/cli.py`
  - Action: Wire services behind a simple façade and basic CLI commands
  - Notes: Keep CLI minimal; UI can be added later

- [x] Task 9: Add scaffold tests
  - File: `tests/test_sales_flow.py`
  - Action: Verify checkout, stock deduction, and earnings summary behavior
  - Notes: Use temp SQLite DB for isolated tests

### Acceptance Criteria
- [x] AC 1: Given an initialized DB, when a product is created, then it appears in inventory listing with persisted stock and price.
- [x] AC 2: Given sufficient stock and cash, when a sale is completed, then sale and line items are persisted and stock is reduced correctly.
- [x] AC 3: Given insufficient cash, when a sale is attempted, then checkout fails with a validation error and no data mutation.
- [x] AC 4: Given existing sales, when daily/weekly/monthly earnings are queried, then totals and transaction counts are returned correctly.
- [ ] AC 5: Given existing products and sales, when CSV export runs, then CSV files are generated with expected headers and rows.
- [x] AC 6: Given this scaffold, when tests run, then core MVP logic passes in a clean environment.

## Additional Context

### Dependencies
- Python 3.11+
- SQLite (stdlib `sqlite3`)
- `unittest` for tests

### Testing Strategy
- Unit/functional tests for core service methods
- Temp-file SQLite database per test case
- Manual smoke run via CLI for DB initialization and list operations

### Notes
- This scaffold is backend/domain-focused and intentionally UI-agnostic.
- Remaining MVP work is tracked in `docs/paw-pos-mvp-backlog.md`.
