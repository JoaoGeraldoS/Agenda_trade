from fastapi import APIRouter, status, Depends
from ...schemas.users.user_schema import CreateUserSchema, LoginUserSchema, ReturnUserSchema
from app.services.users.user_service import UserService
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=ReturnUserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(user: CreateUserSchema, user_service: UserService = Depends()):
    return await user_service.create_user(user)


@router.post("/login")
async def login_user(login_schema: LoginUserSchema, db: UserService = Depends()):
    return await db.login_user(login_schema)


@router.post("/login-form")
async def login_form(form_data: OAuth2PasswordRequestForm = Depends(), db: UserService = Depends()):
    return await db.login_form(form_data)
