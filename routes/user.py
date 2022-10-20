from fastapi import APIRouter
from fastapi import Request

from fastapi.responses import RedirectResponse
import json

# base de datos
import psycopg2
from psycopg2 import Error
from config.db import cursor, db


user = APIRouter()


@user.get("/")
async def root():
    print("Consulta lanzada")
    cursor.execute("SELECT * from coders ;")
    rows = cursor.fetchall()

    #cursor.close()
    #db.close()
    return rows



@user.get("/add/{gender}")
async def add(request: Request, gender: str,):
    #aa = "El Camuñas"
    aa = gender
    print(gender)
    cursor.execute(
        f"INSERT INTO coders (nombre, apellido,ay_la_fruta,Idbootcamp,talento_oculto) values('{aa}','Monsky','Piña',1,'Bailar'); ")
    db.commit()
    #cursor.close()
    #db.close()


@user.get("/consulta")
async def consulta():
    print("Consulta lanzada")
    cursor.execute("SELECT * from coders ;")
    rows = cursor.fetchall() 
        #cursor.close()
        #db.close()
    return rows



@user.get("/")
async def raiz(request: Request):
    sin_codificar = json.dumps(datos)
    json_datos = json.loads(sin_codificar)
    return templates.TemplateResponse("inicio.html", {"request": request, "listado": json_datos})


# Consulta IA
@user.get("/ec/{IA}")
async def read_user_item(request: Request,
                         gender: str
                         ):

    print(gender)
    return f"{resultado:{gender} }"
#cursor.close()
#db.close()
