from fastapi import APIRouter
from db import cursor,db

user = APIRouter()

@user.get("/")
async def root():
    cursor.execute("SELECT * from usuarios ;")
    rows = cursor.fetchall()
    for row in rows:
        print(f" ->", row[1] )
    return {"message": f"{rows}"}


@user.get("/buscar/{item_id}")
# http://127.0.0.1:8000/buscar/usuarios
async def buscar(item_id: str):
    cursor.execute(f"SELECT * from {item_id}")
    rows = cursor.fetchall()
    return rows


@user.get("/buscar/nombre/{nombre}")
# http://127.0.0.1:8000/buscar/nombre/Pepito
async def buscar(nombre: str):
    cursor.execute(f"SELECT * FROM usuarios E FULL JOIN interacciones D ON E.id_usuario = D.Id_usuario FULL JOIN publicaciones P ON E.id_usuario = P.id_usuario where nombres = '{nombre}' ")
    rows = cursor.fetchall()
    return {"nombre": f"{rows}"}


@user.get("/conteo")
# http://127.0.0.1:8000/conteo
async def conteo():
    cursor.execute(f"SELECT COUNT(DISTINCT nombres) FROM usuarios;")
    rows = cursor.fetchall()
    return {"conteo": f"{rows}"}


# SELECT COUNT(DISTINCT me_gusta) FROM interacciones;
#SELECT COUNT(DISTINCT no_me_gusta) FROM interacciones;
#SELECT COUNT(DISTINCT me_interesa) FROM interacciones;

@user.get("/like")
# http://127.0.0.1:8000/like/
async def like():
    cursor.execute(f"SELECT COUNT(tweets), id_usuario FROM publicaciones GROUP BY id_usuario ORDER BY COUNT(tweets) DESC;")
    rows = cursor.fetchall()
    for row in rows:
        print(f" ->", row[1] )
    return {"like": f"{rows}"}

@user.get("/fecha/{fecha_inicio}/{fecha_final}")
    # http://127.0.0.1:8000/fecha/03-05-2022/06-06-2022
async def fecha(fecha_inicio: str, fecha_final: str):   
    cursor.execute(f"SELECT * FROM publicaciones WHERE fecha_de_publicacion >= '{fecha_inicio}' AND fecha_de_publicacion <= '{fecha_final}' ; ")
    rows = cursor.fetchall()
    for row in rows:
        print(f" ->", row[1] )
    return {"rango_fecha": f"{rows}"}


@user.post("/post/{id_usuario}/{mensaje}")
    # http://127.0.0.1:8000/fecha/03-05-2022/06-06-2022
async def post(id_usuario: str, mensaje: str):   
    cursor.execute(f"INSERT INTO publicaciones (tweets,fecha_de_publicacion ,id_topicos, id_usuario) VALUES  ('{mensaje}', '01-01-2022', 1, {id_usuario}) ; ")
    db.commit()
    return {"posteado id": f"{id_usuario}"}


@user.put("/update/{id_usuario}/{id_publicaciones}/{mensaje}")
    # http://127.0.0.1:8000/update/1/15/samuray
async def post(id_usuario: str, id_publicaciones: str, mensaje: str):   
    cursor.execute(f"UPDATE publicaciones SET tweets = '{mensaje}' WHERE id_usuario = {id_usuario} and id_publicaciones = {id_publicaciones}; ")
    db.commit()
    return {"modificado id": f"{id_publicaciones}"}


@user.delete("/delete/{id_usuario}/{id_publicaciones}")
    # http://127.0.0.1:8000/delete/1/15/
async def post(id_usuario: str, id_publicaciones: str):   
    cursor.execute(f"DELETE From publicaciones WHERE id_publicaciones = {id_publicaciones} and id_usuario = {id_usuario} ; ")
    db.commit()
    return {"borrada id": f"{id_publicaciones}"}
