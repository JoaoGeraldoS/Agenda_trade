from fastapi import APIRouter, Depends, status
from app.dependencies.service import get_user_service
from app.schemas.usersSchema import ReturnUserSchema, CreateUserSchema, LoginUserSchema
from app.services.userService import UserService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/", response_model=ReturnUserSchema, status_code=status.HTTP_201_CREATED)
def create_new_user(user: CreateUserSchema, user_service: UserService = Depends(get_user_service)):
    """
    """

    db_user = user_service.create_user_service(user)
    return db_user


@router.post("/login", status_code=status.HTTP_200_OK)
def user_login(login_schema: LoginUserSchema, user_service: UserService = Depends(get_user_service)):
    return user_service.login_user(login_schema)


@router.post("/login-form", status_code=status.HTTP_200_OK)
def user_login(login_form: OAuth2PasswordRequestForm = Depends(), user_service: UserService = Depends(get_user_service)):
    return user_service.login_form(login_form)