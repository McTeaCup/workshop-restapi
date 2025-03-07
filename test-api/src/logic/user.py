from src.main import user_list
from src.schema.schemas import User
from fastapi import HTTPException, status

def create_user(
        first_name: str,
        last_name: str, 
        age: int,
        email: str | None, 
        store_credit: float | None
        ):

    # Check if user already exists
    user: User
    for user in user_list:
        #FIXME: This does not look too good, make a helper function
        if user.first_name == first_name.upper() and user.last_name == last_name.upper():
            raise HTTPException(
                status_code=status.HTTP_208_ALREADY_REPORTED,
                detail="User already exists"
                )
        

    if store_credit == None:
        store_credit = 0.0

    user_list.append(
        User(
            id=len(user_list),
            first_name=first_name.upper(),
            last_name=last_name.upper(),
            age=age,
            email=email,
            store_credit=store_credit
        )
    )

    return user_list[-1]