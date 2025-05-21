from fastapi import FastAPI
from fastapi.testclient import TestClient
from serving.main import app

client = TestClient(app)

def test_getModel():
    response = client.get("/model")
    assert response.status_code == 200
    assert response.json() == {"model_id": "some_string"}

#Dummy test to check if the test suite is working
def test_dummy():
    assert 1 == 1