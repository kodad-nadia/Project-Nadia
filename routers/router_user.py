import uuid
from fastapi import APIRouter, HTTPException
from classes.schema_dto import User, UserNoID

router = APIRouter(
    tags=["Users"]
)

users = [
    User(id=str(uuid.uuid4()), username="user1", email="user1@example.com"),
    User(id=str(uuid.uuid4()), username="user2", email="user2@example.com"),
    User(id=str(uuid.uuid4()), username="user3", email="user3@example.com")
]

@router.get('/users')
async def get_users():
    return users

@router.post('/users')
async def create_user(given_user: UserNoID):
    new_user = User(id=str(uuid.uuid4()), **given_user.dict())
    users.append(new_user)
    return new_user

@router.get('/users/{user_id}')
async def get_user_by_id(user_id: str):
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.patch('/users/{user_id}')
async def modify_user(user_id: str, modified_user: UserNoID):
    for user in users:
        if user.id == user_id:
            user.username = modified_user.username
            user.email = modified_user.email
            return user
    raise HTTPException(status_code=404, detail="User not found")

@router.delete('/users/{user_id}', status_code=204)
async def delete_user(user_id: str):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return
    raise HTTPException(status_code=404, detail="User not found")


