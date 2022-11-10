
from datetime import datetime, timedelta
from jose import  jwt

# replace it with your 32 bit secret key
SECRET_KEY = "09d25e094faa****************f7099f6f0f4caa6cf63b88e8d3e7"
 
# encryption algorithm
ALGORITHM = "HS256"
 
 
def crea_token(data: dict):
    to_encode = data.copy()
     
    # expire time of the token
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
     
    # return the generated token
    return token
 