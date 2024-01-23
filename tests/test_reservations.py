import json
import uuid
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_reservations():
    response = client.get("/reservations")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_reservation():
    reservation_data = {
        "workspace_id": "workspace4",
        "user_id": "user4",
        "date": "2023-10-20",
        "reserved": True
    }

    response = client.post("/reservations", json=reservation_data)
    assert response.status_code == 200
    assert "id" in response.json()

def test_get_reservation_by_id():
    # Assuming there's at least one reservation in the list
    reservation_id = str(uuid.uuid4())
    response = client.get(f"/reservations/{reservation_id}")
    assert response.status_code == 404  # Assuming the reservation doesn't exist in the initial data

def test_modify_reservation():
    # Assuming there's at least one reservation in the list
    reservation_id = str(uuid.uuid4())
    modified_reservation_data = {
        "workspace_id": "modified_workspace",
        "user_id": "modified_user",
        "date": "2023-10-21",
        "reserved": False
    }

    response = client.patch(f"/reservations/{reservation_id}", json=modified_reservation_data)
    assert response.status_code == 404  # Assuming the reservation doesn't exist in the initial data

def test_delete_reservation():
    # Assuming there's at least one reservation in the list
    reservation_id = str(uuid.uuid4())
    response = client.delete(f"/reservations/{reservation_id}")
    assert response.status_code == 404  # Assuming the reservation doesn't exist in the initial data

