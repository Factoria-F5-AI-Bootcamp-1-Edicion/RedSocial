import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI, Header, HTTPException

from rutas.user import user
import requests



client = TestClient(user)


# @pytest.fixture()
# def setUp(client: TestClient):
# # the necessary setup
#     user_1 = {"username": "Lucy", "hashed_password": get_password_hash("1234"), "role": 1, "disabled": False }    
#     insert_user_1 = insert_user(user_1)
#     response_user_1=client.post("/token", data= {"username": "Lucy", "password": "1234"})
#     header_user_1 = {"Authorization": "Bearer" + response_user_1.json()["access_token"]}
#     #second user
#     user_2={"username": "Nancy", "hashed_password": get_password_hash("1234"), "role": 2, "disabled": False}
#     insert_user_2 = insert_user(user_2)
#     response_user_2=client.post("/token", data= {"username": "Nancy", "password": "1234"})
#     header_user_2 ={"Authorization": "Bearer" + response_user_2.json()["access_token"]}
    
#     yield header_user_1, header_user_2
#     #delete those users from database
#     delete_user("Lucy")
#     delete_user("Nancy")




#1. Ruta Get
def test_read_user():
    response = client.get("/")
    assert response.status_code == 404
    #assert response.json() == {[]}

#2. Login de usuario
def test_login_user():
    response = client.post(
        "/api/v1/login/{User}")
    assert response.status_code == 200

#3. Buscar todos los usuarios
def test_search_users():
    response = client.post("/api/v1/buscar/usuarios?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21icmUiOiJhZG1pbiIsInRva2VuIjoiKzMyNjU0NSIsImV4cCI6MTY2ODU5MTc5Mn0.UIejQEf1MOIfSztJkxb2SuGizolHOn-Vr0PCOBggHZM")
    assert response.status_code == 200
#   

# # def test_search_db():
#     response = client.post("/api/v1/buscar/usuarios?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21icmUiOiJhZG1pbiIsInRva2VuIjoiKzMyNjU0NSIsImV4cCI6MTY2ODUyMDA2NH0.JqMdHec_F8Ypmk0mFtHxNNsJwvKL62HwaA8eeuEA2nM")
#     assert response.status_code == 200
# #     #assert response.json() == {[]}

# # Borrar Usuario
# def test_delete_user():

#     response = client.delete("/api/v1/delete/1/5?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21icmUiOiJhZG1pbiIsInRva2VuIjoiKzMyNjU0NSIsImV4cCI6MTY2ODUxMjQ3N30.tRS0Nz_t1IkG47gmC7Hkz4UaxyvIJ3LJJ9j4WFKSlmc")
#     assert response.status_code == 200



# #Update
# def test_update_user():
#     response = client.put(
#         "http://127.0.0.1:8000/api/v1/update/1/1/5?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21icmUiOiJhZG1pbiIsInRva2VuIjoiKzMyNjU0NSIsImV4cCI6MTY2ODUxMjQ3N30.tRS0Nz_t1IkG47gmC7Hkz4UaxyvIJ3LJJ9j4WFKSlmc")
#     assert response.status_code == 200

# # #Buscar nombre de usuarios
# def test_search_users_names():
#     response = client.post("/api/v1/buscar/nombre/Pepito?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJub21icmUiOiJhZG1pbiIsInRva2VuIjoiKzMyNjU0NSIsImV4cCI6MTY2ODU5MTc5Mn0.UIejQEf1MOIfSztJkxb2SuGizolHOn-Vr0PCOBggHZM")
#     assert response.status_code == 200






    

#Validad Token
def test_val_token():
    
    response = client.post("/valida")

#Crear token
def test_create_token():
    
    response = client.post("/get_token")


















    




    
    
   


