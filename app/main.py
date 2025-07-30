from fastapi import FastAPI
from app.core.dataBase import Base, engine
from app.routers import userRoute, taskRoute, activeRoute, operationRoute, evaluationRouter
from app.handlers.register import register_exception_handler
from app.core.security import cors_origin


app = FastAPI(title="Agenda Trade", description="API de agenda e gerenciamento de trade", version="1.0.0")

cors_origin(app)
register_exception_handler(app)

Base.metadata.create_all(bind=engine)

app.include_router(userRoute.router)
app.include_router(taskRoute.router)
app.include_router(activeRoute.router)
app.include_router(operationRoute.router)
app.include_router(evaluationRouter.router)

