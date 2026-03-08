from __future__ import annotations

import argparse

from paw_pos.app import PawPOSApp


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Paw POS CLI")
    parser.add_argument("--db", required=True, help="Path to sqlite database file")

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("init-db", help="Initialize database schema")
    sub.add_parser("list-products", help="List inventory products")

    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    app = PawPOSApp(args.db)

    if args.command == "init-db":
        print("Database initialized.")
        return 0

    if args.command == "list-products":
        products = app.inventory.list_products()
        if not products:
            print("No products yet.")
            return 0
        for p in products:
            print(f"{p['id']} | {p['sku']} | {p['name']} | {p['price_cents']} | stock={p['stock_qty']}")
        return 0

    parser.error("unknown command")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
