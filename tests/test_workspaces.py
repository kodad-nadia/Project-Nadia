import uuid
from fastapi import FastAPI, HTTPException
from fastapi.testclient import TestClient
from pytest import fixture
from main import app
from classes.schema_dto import WorkspaceNoID

@fixture
def test_app():
    return app

@fixture
def test_client(test_app):
    return TestClient(test_app)

@fixture
def create_workspace():
    workspaces = []

    async def _create_workspace(name: str, capacity: int, location: str):
        new_workspace = WorkspaceNoID(name=name, capacity=capacity, location=location)
        new_workspace.id = str(uuid.uuid4())
        workspaces.append(new_workspace)
        return new_workspace

    return _create_workspace

def test_get_workspaces(test_client, create_workspace):
    # Create test workspaces
    workspace1 = create_workspace(name="Workspace A", capacity=10, location="Location X")
    workspace2 = create_workspace(name="Workspace B", capacity=15, location="Location Y")
    workspace3 = create_workspace(name="Workspace C", capacity=20, location="Location Z")

    # Test get_workspaces endpoint
    response = test_client.get("/workspaces")
    assert response.status_code == 200
    assert response.json() == [workspace.dict() for workspace in [workspace1, workspace2, workspace3]]

def test_create_workspace(test_client, create_workspace):
    # Test create_workspace endpoint
    new_workspace_data = {"name": "New Workspace", "capacity": 5, "location": "New Location"}
    response = test_client.post("/workspaces", json=new_workspace_data)
    assert response.status_code == 200
    assert response.json()["name"] == new_workspace_data["name"]
    assert response.json()["capacity"] == new_workspace_data["capacity"]
    assert response.json()["location"] == new_workspace_data["location"]

def test_get_workspace_by_id(test_client, create_workspace):
    # Create a test workspace
    workspace = create_workspace(name="Test Workspace", capacity=8, location="Test Location")

    # Test get_workspace_by_id endpoint
    response = test_client.get(f"/workspaces/{workspace.id}")
    assert response.status_code == 200
    assert response.json()["id"] == workspace.id

def test_modify_workspace(test_client, create_workspace):
    # Create a test workspace
    workspace = create_workspace(name="Test Workspace", capacity=8, location="Test Location")

    # Test modify_workspace endpoint
    modified_data = {"name": "Modified Workspace", "capacity": 12, "location": "Modified Location"}
    response = test_client.patch(f"/workspaces/{workspace.id}", json=modified_data)
    assert response.status_code == 200
    assert response.json()["name"] == modified_data["name"]
    assert response.json()["capacity"] == modified_data["capacity"]
    assert response.json()["location"] == modified_data["location"]

def test_delete_workspace(test_client, create_workspace):
    # Create a test workspace
    workspace = create_workspace(name="Test Workspace", capacity=8, location="Test Location")

    # Test delete_workspace endpoint
    response = test_client.delete(f"/workspaces/{workspace.id}")
    assert response.status_code == 204

    # Check that the workspace has been deleted
    response = test_client.get(f"/workspaces/{workspace.id}")
    assert response.status_code == 404
