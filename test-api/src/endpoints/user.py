from src.main import user_list
from fastapi import APIRouter, HTTPException, status, Response
from src.schema.schemas import User
from src.logic import user
from src.tags import *

user_router = APIRouter()

# ----------------------- GET REQUESTS ----------------------- #

@user_router.get("/", tags=USE_TAGS["admin"])
def get_users():
    """
    Return a full list of all the registered users.
    """
    return user_list

@user_router.get("/id/{user_id}", tags=USE_TAGS["admin"])
def get_user(user_id:int):
    """
    Returns information based on a name.
    """
    if user_id > len(user_list):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user can not be found or does not exist")

    return user_list[user_id]

@user_router.get("/name/{name}", tags=USE_TAGS["admin"])
def get_user_by_name(name:str):

    if not name.strip():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Name not specified")
    print(name.upper not in user_list)
    
    # FIXME: This works but will be crazy inefficient on a large db...
    user: User
    for user in user_list:
        if user.first_name == name.upper() or user.last_name == name.upper():
            break
        elif user.first_name == user_list[-1].first_name:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User could not be found or does not exist"
            )
    
    users = []
    user:User
    for user in user_list:
        if user.first_name.upper() == name.upper() or user.last_name.upper() == name.upper():
            users.append(user)

    return users

# ----------------------- POST REQUESTS ----------------------- #

@user_router.put("/create", tags=USE_TAGS["admin"])
def create_user(
    first_name:str,
    last_name:str,
    age: int,
    email: str | None = None,
    store_credit: float | None = None
    ):
    
    if not first_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="first name not specified"
        )
    if not last_name:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="last name not specified"
        )
    if not age:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="age name not specified"
        )

    return user.create_user(first_name, last_name, age, email, store_credit)

# ----------------------- PUT REQUESTS ----------------------- #
