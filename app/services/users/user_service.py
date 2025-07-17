from fastapi import Depends
from app.db.session import get_db
from app.models.user.user_model import User
from app.schemas.users.user_schema import CreateUserSchema, LoginUserSchema
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.errors import erros_exptions
from app.middlewares.security import pwt_hash, authenticate_user, create_token
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta


class UserService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
    

    async def create_user(self, user_schema: CreateUserSchema):
        user_exist = self.db.execute(select(User).where(User.username == user_schema.username)).scalars().one_or_none()

        if user_exist:
            raise erros_exptions.IsNotNoneException("Usuario ja existe!")


        password_crypt = pwt_hash(user_schema.password)

        new_user = User()
        new_user.name = user_schema.name
        new_user.username = user_schema.username
        new_user.password = password_crypt

        self.db.add(new_user)
        self.db.commit()
        
        return new_user
    
    
    async def login_user(self, login_schema: LoginUserSchema):
        user_exist = self.db.execute(select(User).where(User.username == login_schema.username)).scalars().one_or_none()

        if not user_exist:
            raise erros_exptions.InvalidCredentials("Username ou senha invalidos")
        
        user_authenticate = authenticate_user(user_exist, login_schema.password)

        if not user_authenticate:
            raise erros_exptions.InvalidCredentials("Username ou senha invalidos")
        
        access_token = create_token(user_exist.username)
        refresh_token = create_token(user_exist.username, duration_token=timedelta(days=7))

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
        }

        

    async def login_form(self, form_data: OAuth2PasswordRequestForm):
        user_exist = self.db.execute(select(User).where(User.username == form_data.username)).scalars().one_or_none()

        if not user_exist:
            raise erros_exptions.InvalidCredentials("Username ou senha invalidos")
        
        user_authenticate = authenticate_user(user_exist, form_data.password)

        if not user_authenticate:
            raise erros_exptions.InvalidCredentials("Username ou senha invalidos")
        
        access_token = create_token(user_exist.username)

        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
        
