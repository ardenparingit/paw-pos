from __future__ import annotations

import sqlite3
from datetime import date

from paw_pos.models import EarningsSummary


class EarningsService:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def summarize(self, period: str, anchor: date | None = None) -> EarningsSummary:
        anchor = anchor or date.today()

        if period == "daily":
            where = "date(s.sold_at) = ?"
            args = (anchor.isoformat(),)
        elif period == "weekly":
            # Monday-based week window.
            start = anchor.fromordinal(anchor.toordinal() - anchor.weekday())
            end = start.fromordinal(start.toordinal() + 6)
            where = "date(s.sold_at) BETWEEN ? AND ?"
            args = (start.isoformat(), end.isoformat())
        elif period == "monthly":
            month_prefix = f"{anchor.year:04d}-{anchor.month:02d}-"
            where = "substr(date(s.sold_at), 1, 8) = ?"
            args = (month_prefix,)
        else:
            raise ValueError("period must be one of: daily, weekly, monthly")

        row = self.conn.execute(
            f"""
            SELECT
              COALESCE(SUM(s.total_cents), 0) AS gross,
              COUNT(DISTINCT s.id) AS tx_count,
              COALESCE(SUM(si.quantity), 0) AS line_items
            FROM sales s
            LEFT JOIN sale_items si ON si.sale_id = s.id
            WHERE {where}
            """,
            args,
        ).fetchone()

        return EarningsSummary(
            period=period,
            gross_cents=int(row["gross"]),
            transactions=int(row["tx_count"]),
            line_items=int(row["line_items"]),
        )
