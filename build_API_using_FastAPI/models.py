from pydantic import BaseModel

class Item(BaseModel):
    id : int
    item_name : str
    item_category : str
    item_price : float
