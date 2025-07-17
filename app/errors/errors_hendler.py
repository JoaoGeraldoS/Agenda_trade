from fastapi import Request, status
from fastapi.responses import JSONResponse
from app.errors import erros_exptions

def error_exception(app):
    @app.exception_handler(erros_exptions.IsNotNoneException)
    async def not_none(request: Request, exc: erros_exptions.IsNotNoneException):
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": exc.message})
    
    @app.exception_handler(erros_exptions.InvalidCredentials)
    async def invalid_credentials(request: Request, exc: erros_exptions.InvalidCredentials):
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": exc.message})