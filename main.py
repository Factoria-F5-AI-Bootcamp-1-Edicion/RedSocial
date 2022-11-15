from fastapi import FastAPI
from rutas.user import user

app = FastAPI(
    title="Documentación API YouLive",
    description= """
    
# Nosotros
Somos YouLive, una app que sirve como herramienta de comunicación  bidireccional entre los usuarios que la utilizan.


El usuario puede interactuar, comunicarse  y opinar sobre cualquier asunto de una forma rápida, sencilla y gratuita.
El éxito de nuestra API reside en poder conectarse a otras app y de esa forma ser parte de diversos proyectos en el 
campo de las redes sociales.

![logo_youlive](https://mark.trademarkia.com/logo-images/gesila-group-hk-limited/youlive-86926778.jpg)

Equipo creador: [`NetLab`](https://app.pitch.com/app/presentation/eadcca52-a32b-4e1f-a9e5-f5f06cd79249/1879441d-0772-411e-94bd-c487119cad2f/6da73414-4a2b-4346-8ad6-085638a4e11e "Conócenos").
___
# Objetivo
El propósito de la documentación de nuestra API es brindar una buena experiencia al usuario. Por lo que queremos hacer 
de esta un *guía rápida*. 
___
# Información 
![information](https://cdn.business2community.com/wp-content/uploads/2014/08/data-funnel.png)
## API REST


Nuestra API o *interfaz de programación de aplicaciones*, define cómo las aplicaciones
o los dispositivos pueden conectarse y comunicarse entre sí. 


El concepto REST o *transferencia de estado representacional*, se basa en la filosofía
de una arquitectura flexible ya que la API tipo REST se puede desarrollar utilizando
prácticamente cualquier lenguaje de programación y permite dar soporte a una amplia 
variedad de formatos de datos. A comparación de otras infraestructuras estrictas para
los desarrolladores. 
 
En este caso, nuestra API REST está desarrollada en lenguaje de programación 
[`Python`](https://www.python.org/ "Documentación") y nos devuelve información en formato 
`Json`, uno de los formatos más usados en el desarrollo de apps.


*Formato Json, ejemplo:*

~~~
{
    "message": "Hello World",
    "switch1": "China",
    "switch2": "Germany"
}
~~~

## Librerías
Para el desarollo de nuestra API usamos el marco web moderno y rápido de alto rendimiento
de [`FastAPI`](https://fastapi.tiangolo.com/ "Documentación") basado en sugerencias de
tipo estándar de [Python](https://www.python.org/ "Documentación"). 


A su vez, se utilizó otras librerías que se instalaron con el administrador de paquetes ´Pip´.
Librerías que se usaron:

~~~
pip install fastapi
~~~

~~~
pip install pydantic
~~~

~~~
pip install psycopg2
~~~

~~~
pip install os
~~~

~~~
pip install jose
~~~

~~~
pip install fjwt
~~~

~~~
pip install dotenv
~~~

~~~
pip install colorama
~~~

~~~
pip install db
~~~
___
# Servicios 
La siguiente **ruta raíz** contiene nuestros servicios:

**http://127.0.0.1:8000/api/v1/**


+ [x] Accede a información del usuario desde la base de datos.
+ [x] Ingresa comentarios nuevos.
+ [x] Actualiza comentarios ya existentes.
+ [x] Borra comentarios. 

## Parámetros
Los parámetros usados en esta API son de dos tipos:
+ Parámetros de consulta (query).
+ Parámetros de ruta (path).


## Métodos
Nuestra API gestiona los siguientes métodos HTTP:

- **GET :** solicitar información.
- **POST :** enviar nueva información.
- **PUT :** actualizar información que ya existe.
- **DELETE :** borrar un recurso. 


![metodos](https://phpenthusiast.com/theme/assets/images/blog/what_is_rest_api.png)

## Tabla
En la siguiente tabla especifíca la URL, el método y los páramentros de cada petición implementada:

| Servicios  |       Búsqueda de usuarios                   |             Comentarios nuevos                            |           Actualización de comentarios                                      |                     Eliminar comentarios                           |
| ---------- |       --------------------                   | ----------------------------------------------------------| ----------------------------------------------------------------------------| -------------------------------------------------------------------|
| URL        |http://127.0.0.1:8000/api/v1/buscar/{todos_id}|http://127.0.0.1:8000/api/v1/post/{id_usuario}/{mensaje}|http://127.0.0.1:8000/api/v1/update/{id_usuario}/{id_publicaciones}/{mensaje}   | http://127.0.0.1:8000/api/v1/delete/{id_usuario}/{id_publicaciones}|
| Métodos    |              POST                            |                     POST                                  |                              PUT                                            |                                DELETE                              |
| Parámetros |              path y query                    |                        path y query                      |                             path y query                                     |                path y query                                        |                                           |

___
# Autenticación
+ **Autenticación basada en token:** se debe enviar el token codificado en cada petición HTTP.
![autenticacion](https://www.arsys.es/blog/file/uploads/2018/07/flujo-token.jpg)

## Códigos de estado
Códigos del servidor que indican el estado de nuestra petición:
+ 200: todo fue exitoso.
    + 201: recurso nuevo creado.
+ 400: solicitud inválida. 
    + 422: entidad no procesable.
+ 500: errores del servidor.
___
# Buenas prácticas

+ **Seguridad:** API privada con el fin de que no manipulen ni extraigan la base de datos. 
+ **Testeo:** fiabilidad en el funcionamiento de la API. 
+ **Documentación:** interfaz de documentación con el fin de que sirva como una guía para los usuarios. 

___
# Equipo
![Chen](https://raw.githubusercontent.com/Alexandra121297/Pr-cticaGit/8e74c41c1fd608e1b1b2915473ed52224f28b081/White%20and%20blue%20collage%20hello%20summer%20Instagram%20post.png) 
""",
    version="0.0.1",
    contact={
        "name": "NetLab",
        "url": "https://github.com/Factoria-F5-AI-Bootcamp-1-Edicion/RedSocial",
        "email": "netlab@gmail.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },

)

app.include_router(user)
app.include_router(user)

