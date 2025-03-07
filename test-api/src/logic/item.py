from src.main import item_list
from src.tags import *
from src.schema.schemas import Item
from typing import Union

def create_item(name:str, price:int, quantity:Union[int | None] = 0) -> Item:
    """
    Creates a item in the schema of the "Item" class and adds it to the list of names of items.
    """
    item_list.append(
    Item(
        id=len(item_list),
        name=name,
        price=price,
        quantity=quantity))

    return name

def update_item(id: int, name:str | None, price: int | None, quantity: int | None) -> Item:
    """
    Updates an item in the list based on parameter and index
    """
    # Get item from list of items
    item: Item = item_list[id]

    # Change specified property
    if name != None:
        item.name = name
    if price != None:
        item.price = price
    if quantity != None:
        item.quantity
 
    item_list[id] = item

    return item

def remove_item(value:str):
    """
    Removes an item from the item list it exists.

    Returns:
    - 200 - If item exists
    - 410 - Item was not found or has been deleted previously
    """
    item:Item

    for item in item_list:

        #Can value be phased to int?
        if value.isdigit() and item.id == int(value):
            item_list.remove(item)
            return {
                'status' : 200,
                'message' : f"item {item.name} does no longer exit",
                'context' : "id",
                'item' : item.model_dump()
            }
        
        #Does the name of the item exist?
        elif value.isalnum() and item.name == value:
            if item in item_list:
                    item_list.remove(item)
                    return {
                        'status' : 200,
                        'message' : f"item {item.name} does no longer exit",
                        'context' : "name",
                        'item' : item.model_dump()
                    } 
    
    return {
           'status' : 410,
           'message' : "item does no longer exists",
           'context' : value,
           'item' : f"item id: {value}"
        }