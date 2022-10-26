from fastapi import FastAPI
from rutas.user import user

app = FastAPI()
app.include_router(user)

