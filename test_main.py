from fastapi.testclient import TestClient
import requests
from main import app
#from rutas.user import user

client = TestClient(app) 

def test_get_root():
    response = client.get('/')
    assert response.status_code == 404
  

def test_create_item():
    response = client.post(
        "/api/v1/login/Pepito")
    assert response.status_code == 200
    