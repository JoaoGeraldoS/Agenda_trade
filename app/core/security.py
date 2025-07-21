from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from app.models.users import User
from datetime import timedelta, timezone, datetime
from jose import jwt
from fastapi.security import OAuth2PasswordBearer
from app.core.config import SECRET_KEY, ALGORITHM
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


oauth_schema = OAuth2PasswordBearer(tokenUrl="/user/login-form")
pwt = PasswordHasher()

def pwt_hash(password: str) -> str:
    return pwt.hash(password)


def authenticate_user(user: User, password: str) -> User | bool:
    if not user:
        return False

    try:
        pwt.verify(user.hash_password, password)
        return user
    except VerifyMismatchError:
        return False


def create_token(username: str, duration_token = timedelta(minutes=30)) -> str:
    date_expired = datetime.now(timezone.utc) + duration_token
    date_info = {"sub": username, "exp": date_expired}
    token = jwt.encode(date_info, SECRET_KEY, ALGORITHM)
    return token

def cors_origin(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins="http://127.0.0.1:5500",
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )