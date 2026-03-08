from __future__ import annotations

import sqlite3
from datetime import datetime

from paw_pos.models import SaleLine, SaleResult


class SalesService:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def create_sale(self, lines: list[SaleLine], cash_received_cents: int, sold_at: datetime | None = None) -> SaleResult:
        if not lines:
            raise ValueError("at least one sale line is required")
        if cash_received_cents < 0:
            raise ValueError("cash_received_cents must be >= 0")

        total = 0
        normalized: list[tuple[int | None, str, int, int]] = []

        for line in lines:
            if line.quantity <= 0:
                raise ValueError("quantity must be > 0")
            if line.product_id is None and line.name is None:
                raise ValueError("manual line must include name")

            if line.product_id is not None:
                product = self.conn.execute(
                    "SELECT name, price_cents, stock_qty FROM products WHERE id = ?",
                    (line.product_id,),
                ).fetchone()
                if not product:
                    raise ValueError(f"product_id {line.product_id} not found")
                if int(product["stock_qty"]) < line.quantity:
                    raise ValueError(f"insufficient stock for product_id {line.product_id}")
                name = str(product["name"])
                unit_price = int(product["price_cents"])
            else:
                name = str(line.name)
                unit_price = line.unit_price_cents

            if unit_price < 0:
                raise ValueError("unit_price_cents must be >= 0")

            line_total = unit_price * line.quantity
            total += line_total
            normalized.append((line.product_id, name, line.quantity, unit_price))

        if cash_received_cents < total:
            raise ValueError("cash received is insufficient")

        change = cash_received_cents - total
        sold_at = sold_at or datetime.now()

        with self.conn:
            cur = self.conn.execute(
                """
                INSERT INTO sales (total_cents, cash_received_cents, change_cents, sold_at)
                VALUES (?, ?, ?, ?)
                """,
                (total, cash_received_cents, change, sold_at.isoformat()),
            )
            sale_id = int(cur.lastrowid)

            for product_id, name, quantity, unit_price in normalized:
                line_total = quantity * unit_price
                self.conn.execute(
                    """
                    INSERT INTO sale_items (sale_id, product_id, line_name, quantity, unit_price_cents, line_total_cents)
                    VALUES (?, ?, ?, ?, ?, ?)
                    """,
                    (sale_id, product_id, name, quantity, unit_price, line_total),
                )

                if product_id is not None:
                    self.conn.execute(
                        "UPDATE products SET stock_qty = stock_qty - ?, updated_at = datetime('now') WHERE id = ?",
                        (quantity, product_id),
                    )

        return SaleResult(
            sale_id=sale_id,
            total_cents=total,
            cash_received_cents=cash_received_cents,
            change_cents=change,
            sold_at=sold_at,
        )
