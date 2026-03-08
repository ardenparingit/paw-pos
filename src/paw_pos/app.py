from __future__ import annotations

from pathlib import Path

from paw_pos.db import connect, initialize_schema
from paw_pos.services.earnings import EarningsService
from paw_pos.services.inventory import InventoryService
from paw_pos.services.sales import SalesService


class PawPOSApp:
    """Facade for MVP domain operations."""

    def __init__(self, db_path: str | Path) -> None:
        self.conn = connect(db_path)
        initialize_schema(self.conn)
        self.inventory = InventoryService(self.conn)
        self.sales = SalesService(self.conn)
        self.earnings = EarningsService(self.conn)
