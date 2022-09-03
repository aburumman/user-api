from fastapi.testclient import TestClient

from user_api import app

client = TestClient(app)

def test_user_by_id():
    response = client.get("/users/{id}")
    assert response.status_code == 200
    users = response.json()
    assert users.id == 1
    #assert all(["name" in user for user in users])
