from fastapi import FastAPI
from .routers.users import user_router
from app.routers.tasks import task_router
from app.errors.errors_hendler import error_exception
from app.middlewares.security import cors_origin

app = FastAPI()


cors_origin(app=app)
error_exception(app=app)

app.include_router(user_router.router)
app.include_router(task_router.router)


