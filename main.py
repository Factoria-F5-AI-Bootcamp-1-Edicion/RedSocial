from fastapi import FastAPI, status
from rutas.user import user


app = FastAPI()
app.include_router(user)

# logging.debug('go to log file')
# logging.info('for informations')
# logging.warning('and this for worning')
# logging.error('for error')