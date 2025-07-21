from app.repositories.usersRepository import UserRepository
from app.schemas.usersSchema import CreateUserSchema, LoginUserSchema, ReturnUserSchema
from app.core.security import pwt_hash
from app.exceptions.users import UserExists, UserInvalideCredentials
from app.exceptions.generic_exeption import NotFound
from app.core.security import authenticate_user
from app.core.security import create_token
from fastapi.security import OAuth2PasswordRequestForm


class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def create_user_service(self, user: CreateUserSchema) -> ReturnUserSchema:
        userExists = self.user_repo.get_by_username(user.username)

        if userExists:
            raise UserExists("Usuario já existe")

        user_data = user.model_dump(exclude={"password"})
        user_data["hash_password"] = pwt_hash(user.password)

        create_user = self.user_repo.create_user(user_data)
        self.user_repo.db.commit()
        return ReturnUserSchema.model_validate(create_user)
    

    
    def login_user(self, login_schema: LoginUserSchema) -> dict:
        userExists = self.user_repo.get_by_username(login_schema.username)

        if not userExists:
            raise NotFound("Usuario não existente")
        
        user_authenticate = authenticate_user(userExists, login_schema.password)

        if not user_authenticate:
            raise UserInvalideCredentials("Username ou Senha invalidos")
        
        access_token = create_token(userExists.username)

        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }


    def login_form(self, login_form: OAuth2PasswordRequestForm) -> dict:
        userExists = self.user_repo.get_by_username(login_form.username)

        if not userExists:
            raise NotFound("Usuario não existente")
        
        user_authenticate = authenticate_user(userExists, login_form.password)

        if not user_authenticate:
            raise UserInvalideCredentials("Username ou Senha invalidos")
        
        access_token = create_token(userExists.username)

        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
