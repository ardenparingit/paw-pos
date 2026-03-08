from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class SaleLine:
    """One line in a sale; can be catalog-backed or manual."""

    quantity: int
    unit_price_cents: int
    product_id: int | None = None
    name: str | None = None


@dataclass(slots=True)
class SaleResult:
    sale_id: int
    total_cents: int
    cash_received_cents: int
    change_cents: int
    sold_at: datetime


@dataclass(slots=True)
class EarningsSummary:
    period: str
    gross_cents: int
    transactions: int
    line_items: int
