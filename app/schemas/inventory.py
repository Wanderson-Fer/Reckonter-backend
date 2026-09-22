from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class InventoryCreate(BaseModel):
    id_product: int
    quantity: float
    last_update: datetime
    location: Optional[str]

class InventoryResponse(BaseModel):
    id: int
    id_product: int
    quantity: float
    last_update: datetime
    location: Optional[str]
