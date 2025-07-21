from app.dependencies.get_db import get_db
from app.repositories.usersRepository import UserRepository
from app.repositories.taskRepository import TaskRepository
from app.repositories.activeRepository import ActiveRepository
from fastapi import Depends
from sqlalchemy.orm import Session

from app.services.userService import UserService
from app.services.taskService import TaskService
from app.services.activeService import ActiveService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    user_repo = UserRepository(db)

    return UserService(user_repo)

def get_task_service(db: Session = Depends(get_db)) -> TaskService:
    task_repo = TaskRepository(db)
    return TaskService(task_repo)

def get_active_service(db: Session = Depends(get_db)) -> ActiveService:
    trade_repo = ActiveRepository(db)
    return ActiveService(trade_repo)