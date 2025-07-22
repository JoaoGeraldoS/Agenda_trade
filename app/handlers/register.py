from fastapi import FastAPI, HTTPException
from app.exceptions.users import UserExists, UserInvalideCredentials
from app.exceptions.active import ActiveExists
from app.exceptions.generic_exeption import NotFound, BadRequest
from app.handlers.exception_handlers import (
    http_exception_handler, 
    user_exists_handler,
    not_found_handler,
    user_invalid_credentials_handler,
    active_exists_handler, 
    operation_handler
    )


def register_exception_handler(app: FastAPI):

    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(UserExists, user_exists_handler)
    app.add_exception_handler(UserInvalideCredentials, user_invalid_credentials_handler)
    app.add_exception_handler(NotFound, not_found_handler)
    app.add_exception_handler(ActiveExists, active_exists_handler)
    app.add_exception_handler(BadRequest, operation_handler)