import importlib

from fastapi.testclient import TestClient


app = importlib.import_module("1stapi").app
client = TestClient(app)


def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "hello"}


def test_about():
    response = client.get("/about")

    assert response.status_code == 200
    assert response.json() == {"message": "this is about page"}


def test_user():
    response = client.get("/user")

    assert response.status_code == 200
    assert response.json() == {"user": ["akhil", "vip", "reema"]}