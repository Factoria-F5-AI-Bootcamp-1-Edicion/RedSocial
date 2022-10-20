# Importamos librerias necesarias
from fastapi import FastAPI, Request  # servidor
from routes.user import user  # rutas
# variables de entorno
from config.db import cursor, db

#### Pruebas correctas !!!


app = FastAPI()


@app.get('/')
def root():
    cursor.execute("SELECT * from coders ;")
    rows = cursor.fetchall()
    

    return rows

