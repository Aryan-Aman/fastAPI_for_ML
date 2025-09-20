from pydantic import BaseModel, Field, StrictInt
from typing import Optional


class Item(BaseModel):
    id: int = Field(..., gt=0, title="ID must be a positive integer")
    item_name: str = Field(..., min_length=1, max_length=40)
    item_category: str = Field(..., min_length=1, max_length=40)
    item_price: float = Field(..., ge=0.0)
    item_quantity: StrictInt = Field(default=1, ge=0)