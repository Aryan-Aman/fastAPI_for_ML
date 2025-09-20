from fastapi import FastAPI, HTTPException
from models_validn import Item
from typing import List

app = FastAPI()

items_db : List[Item]= []

#read all items
@app.get("/items",response_model=List[Item])
def get_items():
    return items_db


#read single item by id
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            return items_db[idx]
    raise HTTPException(status_code=404, detail="Item not found")

#create item
@app.post("/add_items", response_model=Item)
def create_item(new_item: Item):
    for existing_item in items_db:
        if existing_item.id == new_item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items_db.append(new_item)
    return {"message": "Item created successfully", "item": new_item}
    

#update item
@app.put("/update_items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db[idx] = updated_item
            return {"message": "Item updated successfully", "item": updated_item}
    raise HTTPException(status_code=404, detail="Item not found to update")

#delete item
@app.delete("/items/{item_id}", response_model=dict)
def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            del items_db[idx]
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found to delete")

#clear all items
@app.delete("/items")
def clear_all_items():
    items_db.clear()
    return {"message": "All items cleared"}