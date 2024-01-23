import uuid
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pytest import fixture
from main import app
from classes.schema_dto import UserNoID

@fixture
def test_app():
    return app

@fixture
def test_client(test_app):
    return TestClient(test_app)

@fixture
def create_user():
    users = []

    def _create_user(email: str, username: str):
        new_user = UserNoID(email=email, username=username)
        new_user.id = str(uuid.uuid4())
        users.append(new_user)
        return new_user

    return _create_user

def test_get_users(test_client, create_user):
    # Create test users
    user1 = create_user(email="user1@example.com", username="user1")
    user2 = create_user(email="user2@example.com", username="user2")
    user3 = create_user(email="user3@example.com", username="user3")

    # Test get_users endpoint
    response = test_client.get("/users")
    assert response.status_code == 200
    assert response.json() == [user.dict() for user in [user1, user2, user3]]

def test_create_user(test_client, create_user):
    # Test create_user endpoint
    new_user_data = {"email": "new_user@example.com", "username": "new_user"}
    response = test_client.post("/users", json=new_user_data)
    assert response.status_code == 200
    assert response.json()["email"] == new_user_data["email"]
    assert response.json()["username"] == new_user_data["username"]

def test_get_user_by_id(test_client, create_user):
    # Create a test user
    user = create_user(email="test@example.com", username="test_user")

    # Test get_user_by_id endpoint
    response = test_client.get(f"/users/{user.id}")
    assert response.status_code == 200
    assert response.json()["id"] == user.id

def test_modify_user(test_client, create_user):
    # Create a test user
    user = create_user(email="test@example.com", username="test_user")

    # Test modify_user endpoint
    modified_data = {"email": "modified@example.com", "username": "modified_user"}
    response = test_client.patch(f"/users/{user.id}", json=modified_data)
    assert response.status_code == 200
    assert response.json()["email"] == modified_data["email"]
    assert response.json()["username"] == modified_data["username"]

def test_delete_user(test_client, create_user):
    # Create a test user
    user = create_user(email="test@example.com", username="test_user")

    # Test delete_user endpoint
    response = test_client.delete(f"/users/{user.id}")
    assert response.status_code == 204

    # Check that the user has been deleted
    response = test_client.get(f"/users/{user.id}")
    assert response.status_code == 404

