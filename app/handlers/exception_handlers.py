from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from app.exceptions.users import UserExists, UserInvalideCredentials
from app.exceptions.generic_exeption import NotFound
from app.exceptions.active import ActiveExists


async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": {
                "status_code": exc.status_code,
                "detail": exc.detail,
                "path": str(request.url.path),
                "method": request.method
            }
        }
    )


async def not_found_handler(request: Request, exc: NotFound):
     return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content= {
            "error": {
                "status_code": status.HTTP_404_NOT_FOUND,
                "detail": exc.message,
                "path": str(request.url.path),
                "method": request.method
            }
        }
    )


async def user_exists_handler(request: Request, exc: UserExists):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content= {
            "error": {
                "status_code": status.HTTP_409_CONFLICT,
                "detail": exc.message,
                "path": str(request.url.path),
                "method": request.method
            }
        }
    )


async def active_exists_handler(request: Request, exc: ActiveExists):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content= {
            "error": {
                "status_code": status.HTTP_409_CONFLICT,
                "detail": exc.message,
                "path": str(request.url.path),
                "method": request.method
            }
        }
    )


async def user_invalid_credentials_handler(request: Request, exc: UserInvalideCredentials):
    return JSONResponse(
        status_code=status.HTTP_401_UNAUTHORIZED,
        content= {
            "error": {
                "status_code": status.HTTP_401_UNAUTHORIZED,
                "detail": exc.message,
                "path": str(request.url.path),
                "method": request.method
            }
        }
    )

