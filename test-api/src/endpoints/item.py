from fastapi import APIRouter, HTTPException, status, Response
from typing import Union
from src.main import item_list
from src.tags import *
import src.logic.item as item_logic

item_router = APIRouter()

# ----------------------- GET REQUESTS ----------------------- #

test = "YO WHAT UP"

#Get all items
@item_router.get("/", tags=USE_TAGS["customer"])
def get_items() -> list:
    """
    Returns a of all items and information regarding them.
    """
    return item_list

#Get item
@item_router.get("/{item_id}", tags=USE_TAGS["customer"])
def get_item(item_id:int):
    """
    Returns a dictionary of a specific item.
    """
    if(item_id > len(item_list)):
        raise HTTPException(status_code=404, detail="Item ID not found")
    return item_list[item_id]

# ----------------------- POST REQUESTS ----------------------- #

#Create new item
@item_router.post("/add-item", tags=USE_TAGS["admin"], status_code=201)
def create_item(name:str, price:float, quantity:Union[int, None] = None):
    """
    Creates a item in the list.
    
    *Parameters*
    - **name**
    - **price**
    - **quantity**
    """
    # If item has no name or is just spaces, throw 400 error
    if not name.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="name can not be empty")
    
    item = item_logic.create_item(name, price, quantity)
    
    return {
        'status' : status.HTTP_201_CREATED,
        'message' : f"Added {name} to the list of items",
        'item' : item
        }

# ----------------------- PUT REQUESTS ----------------------- #

@item_router.put("/{item_id}", tags=USE_TAGS["admin"])
def update_item(
    item_id:int,
    name: str | None = None,
    price: int | None = None,
    quantity: int | None = None):
    """
    Updates a specified item in the list.
    """
    if type(item_id) != int:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="id of item was not specified"
        )
    if name == None and price == None and quantity == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="no new values of item's properties was specified"
        )

    new_item = item_logic.update_item(item_id, name, price, quantity)

    return {
        'status' : status.HTTP_200_OK,
        'message' : f"Item '{item_id}' was successfully updated!",
        'item' : new_item
    }
    pass

# ----------------------- DELETE REQUESTS ----------------------- #

@item_router.delete("/remove/{item_id}", tags=USE_TAGS["admin"])
def remove_item(item_id: Union[int, str] = int):
    
    # Is item string or number?
    if type(item_id) != str and type(item_id) != int:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="only item ID or item name can be specified")

    # Is id out of bounds?
    if type(item_id) == int and item_id > len(item_list):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="incorrect value type, only type int is accepted")

    return item.remove_item(item_id)