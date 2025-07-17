from fastapi import Depends
from jose import jwt, JWTError
from app.middlewares.security import SECRET_KEY, ALGORITHM, oauth_schema
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user.user_model import User
from app.errors import erros_exptions
from sqlalchemy import select

def verify_token(token: str = Depends(oauth_schema), db: Session = Depends(get_db)):
    try:
        data_info = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        data = data_info.get("sub")
    except JWTError:
        raise erros_exptions.InvalidCredentials("Acesso negado")
    
    user = db.execute(select(User).where(User.username==data)).scalars().one_or_none()

    if not user:
        raise erros_exptions.InvalidCredentials("Acesso negado")
    
    return user