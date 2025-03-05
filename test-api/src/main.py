import random
from src.schema.schemas import *
from src.tags import *

item_list = []
user_list = []

def generate_items(id:int, name: str) -> Item:
    return Item(
        id=id, 
        name=name, 
        price=random.randrange(1, 50), 
        quantity=random.randrange(0, 1000))

def generate_users(id:int, name:str):
    mail_service = MAIL_SERVICES[random.randrange(0, len(MAIL_SERVICES))]
    return User(
        id=id,
        first_name=name.split(" ")[0],
        last_name=name.split(" ")[1],
        email=f"{name.split(" ")[0].lower()}.{name.split(" ")[1].lower()}@{mail_service}.com",
        age=random.randrange(18,90),
        store_credit=random.randrange(0,1000)
    )

for item in ITEM_NAMES:
    item_list.append(generate_items(id=len(item_list), name=item))

for user in USER_NAMES:
    user_list.append(
        generate_users(
            id=len(user_list),
            name=user
        ))