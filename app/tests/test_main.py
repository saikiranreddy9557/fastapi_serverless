
from fastapi.testclient import TestClient
from app.main import app




client = TestClient(app)


def test_sample():
    response = client.get("/")
    print(response)
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}
    