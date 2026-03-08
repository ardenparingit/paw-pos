from __future__ import annotations

import os
import tempfile
import unittest
from datetime import date

from paw_pos.app import PawPOSApp
from paw_pos.models import SaleLine


class SalesFlowTests(unittest.TestCase):
    def setUp(self) -> None:
        fd, path = tempfile.mkstemp(prefix="paw-pos-", suffix=".sqlite3")
        os.close(fd)
        self.db_path = path
        self.app = PawPOSApp(self.db_path)

    def tearDown(self) -> None:
        try:
            os.remove(self.db_path)
        except FileNotFoundError:
            pass

    def test_sale_deducts_stock_and_updates_daily_earnings(self) -> None:
        product_id = self.app.inventory.upsert_product(
            sku="DOG-FOOD-1",
            name="Dog Food",
            price_cents=25000,
            stock_qty=10,
        )

        result = self.app.sales.create_sale(
            lines=[SaleLine(product_id=product_id, quantity=2, unit_price_cents=0)],
            cash_received_cents=60000,
        )

        self.assertEqual(result.total_cents, 50000)
        self.assertEqual(result.change_cents, 10000)

        products = self.app.inventory.list_products()
        self.assertEqual(products[0]["stock_qty"], 8)

        summary = self.app.earnings.summarize("daily", anchor=date.today())
        self.assertEqual(summary.gross_cents, 50000)
        self.assertEqual(summary.transactions, 1)
        self.assertEqual(summary.line_items, 2)

    def test_insufficient_cash_rejects_sale(self) -> None:
        product_id = self.app.inventory.upsert_product(
            sku="CAT-TOY-1",
            name="Cat Toy",
            price_cents=10000,
            stock_qty=5,
        )

        with self.assertRaises(ValueError):
            self.app.sales.create_sale(
                lines=[SaleLine(product_id=product_id, quantity=1, unit_price_cents=0)],
                cash_received_cents=5000,
            )


if __name__ == "__main__":
    unittest.main()
