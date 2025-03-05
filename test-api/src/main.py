from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union
import random

app = FastAPI()
ITEM_NAMES = ["milk", "bread", "cerial", "butter", "egg", "tomato"]
item_list = []

class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: Union[int, None] = None 

def generate_items(id:int, name: str) -> Item:
    return Item(id=id, name=name, price=random.randrange(1, 500), quantity=random.randrange(0, 1000))

for item in ITEM_NAMES:
    item_list.append(generate_items(id=len(item_list), name=item))

#Get items
@app.get("/items/{item_id}")
def get_item(item_id:int):
    if(item_id > len(item_list)):
        raise HTTPException(status_code=404, detail="Item ID not found")

    return item_list[item_id]

@app.post("/add-item")
def post_item(name:str, price:float, quantity:Union[int, None] = None):
    
    item_list.append(Item(id=len(item_list), name=name, price=price, quantity=quantity))
    #TODO: Optimize later
    #Add item to item list
    ITEM_NAMES.append(name)
    
    return {'status' : 201, 'message' : f"Added {name} to the list of items"}


