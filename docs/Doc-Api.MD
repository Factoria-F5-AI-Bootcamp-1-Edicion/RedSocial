## Librerias en requerimientos.txt
Se instaln con la version de python 3.x mediante el comando:
pip install -r requerimientos.txt

## Se crea .gitignore en la rama ApiRest

para ocultar el fichero de configuracion de datos sensibles como password de la base de datos, lo guardamos en .env

## Creamos .env
Se crean las variables de entorno 
con los datos, en el fichero.

## Creamos la carpeta config
con los datos para la conexion a la base de datos posgre

## Creamos la carpeta routes
se añade el fichero user.py
desde el que se gestiona los usuarios en:
http://127.0.0.1/user/


## para más pruebas sobre la api
http://127.0.0.1:8000/docs

