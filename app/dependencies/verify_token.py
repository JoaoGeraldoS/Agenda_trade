from jose import jwt, JWTError
from app.core.config import SECRET_KEY, ALGORITHM
from app.core.security import oauth_schema
from sqlalchemy.orm import Session
from .get_db import get_db
from app.models.users import User
from sqlalchemy import select
from fastapi import Depends
from app.exceptions.users import UserInvalideCredentials

def verify_token(token: str = Depends(oauth_schema), db: Session = Depends(get_db)) -> User:
    try:
        date_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        data = date_info.get("sub")
    except JWTError:
        raise UserInvalideCredentials("Erro de acesso")
    
    user = db.execute(select(User).where(User.username == data)).scalars().one_or_none()

    if not user:
        raise UserInvalideCredentials("Erro de acesso")
    
    return user


