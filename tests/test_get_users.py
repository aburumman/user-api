from fastapi.testclient import TestClient

from user_api import app

client = TestClient(app)


def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    users = response.json()
    assert all(["name" in user for user in users])
