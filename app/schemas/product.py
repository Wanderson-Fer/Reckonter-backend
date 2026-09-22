from pydantic import BaseModel
from typing import Optional

from app.schemas.inventory import InventoryCreate, InventoryResponse


class ProductCreate(BaseModel):
    name: str
    description: str
    unit_price: float
    supplier_price: float
    measures: str

    # First inv register (optional)
    inventory: Optional[InventoryCreate] = None

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    unit_price: float
    supplier_price: float
    measures: str

    inventory: Optional[InventoryResponse] = None
