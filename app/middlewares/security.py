import os
from fastapi.security import OAuth2PasswordBearer
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timezone, timedelta
from jose import jwt
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

oauth_schema = OAuth2PasswordBearer(tokenUrl="/user/login-form")
ALGORITHM = os.getenv("ALGORITHM")
SECRET_KEY = os.getenv("SECRET_KEY")

pwt = PasswordHasher()

def pwt_hash(password):
    return pwt.hash(password)


def authenticate_user(user, password: str):
    if not user:
        return False
   
    try:
        pwt.verify(user.password, password)

        return user
    except VerifyMismatchError:
        return False

    
def create_token(username, duration_token = timedelta(minutes=30)):
    date_exired = datetime.now(timezone.utc) + duration_token
    date_info = {"sub": username, "exp": date_exired}
    token = jwt.encode(date_info, SECRET_KEY, ALGORITHM)
    return token

def cors_origin(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins="http://127.0.0.1:5500",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )