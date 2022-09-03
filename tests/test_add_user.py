from fastapi.testclient import TestClient

from user_api import app

client = TestClient(app)

def test_add_user():
    response = client.post("/users/", json={
        "name": "Adetola"})
    user = response.json()
    assert response.status_code == 200
    assert user["name"] == "Adetola"
