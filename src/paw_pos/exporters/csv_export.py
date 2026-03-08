from __future__ import annotations

import csv
import sqlite3
from pathlib import Path


def export_products_csv(conn: sqlite3.Connection, output_path: str | Path) -> Path:
    path = Path(output_path)
    rows = conn.execute(
        "SELECT id, sku, name, price_cents, stock_qty FROM products ORDER BY id"
    ).fetchall()
    with path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow(["id", "sku", "name", "price_cents", "stock_qty"])
        for row in rows:
            writer.writerow([row["id"], row["sku"], row["name"], row["price_cents"], row["stock_qty"]])
    return path


def export_sales_csv(conn: sqlite3.Connection, output_path: str | Path) -> Path:
    path = Path(output_path)
    rows = conn.execute(
        """
        SELECT
          s.id AS sale_id,
          s.sold_at,
          s.total_cents,
          s.cash_received_cents,
          s.change_cents,
          si.product_id,
          si.line_name,
          si.quantity,
          si.unit_price_cents,
          si.line_total_cents
        FROM sales s
        JOIN sale_items si ON si.sale_id = s.id
        ORDER BY s.id, si.id
        """
    ).fetchall()
    with path.open("w", newline="", encoding="utf-8") as fp:
        writer = csv.writer(fp)
        writer.writerow([
            "sale_id",
            "sold_at",
            "total_cents",
            "cash_received_cents",
            "change_cents",
            "product_id",
            "line_name",
            "quantity",
            "unit_price_cents",
            "line_total_cents",
        ])
        for row in rows:
            writer.writerow([
                row["sale_id"],
                row["sold_at"],
                row["total_cents"],
                row["cash_received_cents"],
                row["change_cents"],
                row["product_id"],
                row["line_name"],
                row["quantity"],
                row["unit_price_cents"],
                row["line_total_cents"],
            ])
    return path
