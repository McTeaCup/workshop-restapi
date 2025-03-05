from src.main import item_list
from src.tags import *
from src.schema.schemas import Item
from typing import Union

def create_item(name:str, price:int, quantity:Union[int | None] = 0):
    """
    Creates a item in the schema of the "Item" class and adds it to the list of names of items.

    Returns: Item
    """
    item_list.append(
    Item(
        id=len(item_list),
        name=name,
        price=price,
        quantity=quantity))
    
    #TODO: Optimize later
    #Add item to item list
    ITEM_NAMES.append(name)

    return name

def update_item(id: int, name:str | None, price: int | None, quantity: int | None):
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