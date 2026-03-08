from __future__ import annotations

import sqlite3
from typing import Any


class InventoryService:
    def __init__(self, conn: sqlite3.Connection) -> None:
        self.conn = conn

    def upsert_product(self, sku: str, name: str, price_cents: int, stock_qty: int) -> int:
        if price_cents < 0:
            raise ValueError("price_cents must be >= 0")
        if stock_qty < 0:
            raise ValueError("stock_qty must be >= 0")

        existing = self.conn.execute(
            "SELECT id FROM products WHERE sku = ?",
            (sku,),
        ).fetchone()

        if existing:
            self.conn.execute(
                """
                UPDATE products
                SET name = ?, price_cents = ?, stock_qty = ?, updated_at = datetime('now')
                WHERE id = ?
                """,
                (name, price_cents, stock_qty, int(existing["id"])),
            )
            self.conn.commit()
            return int(existing["id"])

        cur = self.conn.execute(
            """
            INSERT INTO products (sku, name, price_cents, stock_qty)
            VALUES (?, ?, ?, ?)
            """,
            (sku, name, price_cents, stock_qty),
        )
        self.conn.commit()
        return int(cur.lastrowid)

    def list_products(self) -> list[dict[str, Any]]:
        rows = self.conn.execute(
            "SELECT id, sku, name, price_cents, stock_qty FROM products ORDER BY name ASC"
        ).fetchall()
        return [dict(row) for row in rows]

    def adjust_stock(self, product_id: int, delta: int) -> int:
        row = self.conn.execute(
            "SELECT stock_qty FROM products WHERE id = ?",
            (product_id,),
        ).fetchone()
        if not row:
            raise ValueError("product not found")

        new_qty = int(row["stock_qty"]) + delta
        if new_qty < 0:
            raise ValueError("stock cannot go below zero")

        self.conn.execute(
            "UPDATE products SET stock_qty = ?, updated_at = datetime('now') WHERE id = ?",
            (new_qty, product_id),
        )
        self.conn.commit()
        return new_qty
