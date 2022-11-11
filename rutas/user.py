import os
from fastapi import status, HTTPException

from pydantic import BaseModel
from jose import JWTError, jwt
from fjwt import crea_token

from fastapi import APIRouter
from db import cursor,db
## nuevo
import logging

from dotenv import load_dotenv
from colorama import init, Fore, Back

init()
load_dotenv() 
logging.basicConfig(format='%(asctime)s %(message)s', filename='mylog.log', encoding='utf-8', level=logging.DEBUG)
SECRET_KEY = os.environ.get('SECRET_KEY')
ALGORITHM = os.environ.get('ALGORITHM')


class Token(BaseModel):
    access_token: str
    token_type: str
    
    
user = APIRouter(prefix="/api/v1")

data = {
        'nombre': 'admin',
        'token': '+326545'
    }


@user.get("/", status_code=404)
async def root():   
    
    try:
        logging.info('Peticion / redireccion a /api/v1/')
        print(Fore.BLUE, "Get to  /api/v1/")
        
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Could not validate credentials",
        )
        return { "message": "You not have access" }
    except JWTError:
        Warning.info('JWT Error')
        print(Fore.BLUE + "JWT Error")
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        return { "Warning": "JWT Error" }
    finally:
    
        logging.warning('HTTP Exception')
        print(Fore.BLUE + "HTTP Exception")
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
        return { "Warning": "HTTP Exception" }
        


# solo si existe el usuario te da el token.
@user.post("/login/{user}",status_code=200)
async def login(user: str):
    with cursor:    
        cursor.execute(f"SELECT * from usuarios where nombres = '{user}';")
        rows = cursor.fetchall()
        # buscamos el usuario en la base de datos
        for row in rows:
            if f"{user}" in row[1]:
                token = crea_token(data=data)
                return ({'token': {token}})
            else:
                return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials"
            )
    #cursor.close()

@user.post("/buscar/{todos_id}", status_code=200)
# http://127.0.0.1:8000/buscar/usuarios
async def buscar(token: str,todos_id: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #print(payload['nombre'])
        #with cursor:
        cursor.execute(f"SELECT * from {todos_id}")
        rows = cursor.fetchall()
            #if rows.length > 0:
                #cursor.close()   
        #cursor.close()
        return rows #payload
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    #finally:
        #cursor.close()



@user.delete("/delete/{id_usuario}/{id_publicaciones}", status_code=200)
    # http://127.0.0.1:8000/delete/1/15/
async def post(token: str,id_usuario: str, id_publicaciones: str):   
        
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #print(payload['nombre'])
        #with cursor:
        cursor.execute(f"DELETE From publicaciones WHERE id_publicaciones = {id_publicaciones} and id_usuario = {id_usuario} ; ")
        db.commit()
        
        return {"borrada id": f"{id_publicaciones}"}
        
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
            




## revisar no tengo ddbb
@user.put("/update/{id_usuario}/{id_publicaciones}/{mensaje}", status_code=200)
    # http://127.0.0.1:8000/update/1/15/samuray
async def post(token: str,id_usuario: str, id_publicaciones: str, mensaje: str):   
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #print(payload['nombre'])
        with cursor:
            cursor.execute(f"UPDATE publicaciones SET tweets = '{mensaje}' WHERE id_usuario = {id_usuario} and id_publicaciones = {id_publicaciones}; ")
            db.commit()
            cursor.close()
        return {"modificado id": f"{id_publicaciones}"}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
            

@user.post("/post/{id_usuario}/{mensaje}", status_code=status.HTTP_201_CREATED)
    # http://127.0.0.1:8000/post/1/HolaHallowend
async def post(token: str,id_usuario: str, mensaje: str):   
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #print(payload['nombre'])
        with cursor:
            cursor.execute(f"INSERT INTO publicaciones (tweets,fecha_de_publicacion ,id_topicos, id_usuario) VALUES  ('{mensaje}', '01-01-2022', 1, {id_usuario}) ; ")
            db.commit()
        cursor.close()
        return {"posteado id": f"{id_usuario}"}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    

@user.post("/fecha/{fecha_inicio}/{fecha_final}", status_code=200)
    # http://127.0.0.1:8000/fecha/03-05-2022/06-06-2022
async def fecha(token: str,fecha_inicio: str = '03-05-2022',fecha_final: str = '06-06-2022'):   
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #print(payload['nombre'])
        with cursor:
            cursor.execute(f"SELECT * FROM publicaciones WHERE fecha_de_publicacion >= '{fecha_inicio}' AND fecha_de_publicacion <= '{fecha_final}' ; ")
            rows = cursor.fetchall()
        cursor.close()
        return {"rango_fecha": f"{rows}"}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    
  
@user.post("/buscar/nombre/{nombre}", status_code=200)
# http://127.0.0.1:8000/buscar/nombre/Pepito
async def buscar(token: str,nombre: str):
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        #print(payload['nombre'])
        with cursor:
            cursor.execute(f"SELECT * FROM usuarios E FULL JOIN interacciones D ON E.id_usuario = D.Id_usuario FULL JOIN publicaciones P ON E.id_usuario = P.id_usuario where nombres = '{nombre}' ")
            rows = cursor.fetchall()
        cursor.close()
        return {"nombre": f"{rows}"}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )
    

@user.post("/valida")
async def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        with cursor:
            cursor.execute(f"SELECT * from usuarios ;")
            rows = cursor.fetchall()
        cursor.close()
        return rows #payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )



@user.post("/get_token")
async def get_token():  
    token = crea_token(data=data)
    return {'token': token}
