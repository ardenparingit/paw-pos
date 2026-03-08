# Paw POS

Initial Python scaffold for an offline-first POS MVP.

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
