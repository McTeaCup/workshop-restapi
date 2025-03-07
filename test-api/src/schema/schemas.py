from pydantic import BaseModel
from typing import Union

class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: Union[int, None] = None

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    email: str | None
    store_credit: float | None