from fastapi import Depends
from sqlalchemy.orm import Session, join
from sqlalchemy import select
from app.db.session import get_db
from app.schemas.tasks.task_schema import CreateTaskSchema
from app.models.tasks.task_model import Task
from app.models.user.user_model import User
from app.errors import erros_exptions


class TaskService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def read_task(self, id: int):
        tasks = self.db.execute(select(Task).join(User, User.id == Task.user_id).filter(User.id == id))
        return tasks.scalars().all()
    
    
    async def read_unique_task(self, id: int):
        task = self.db.execute(select(Task).where(Task.id == id)).scalars().one_or_none()

        if task is None:
            raise erros_exptions.IsNotNoneException("Tarefa não existe")

        return task


    async def create_task(self, task_schema: CreateTaskSchema, user_id: int):
        new_task = Task()

        new_task.title = task_schema.title
        new_task.description = task_schema.description
        new_task.concluded = task_schema.concluded
        new_task.user_id = user_id

        self.db.add(new_task)
        self.db.commit()

        return new_task


    async def update_task(self, id: int, task_schema: CreateTaskSchema):
        task = await self.read_unique_task(id)

        task.title = task_schema.title
        task.description = task_schema.description
        task.concluded = task_schema.concluded

        self.db.add(task)
        self.db.commit()

        return task
    

    async def update_concluded(self, id: int):
        task = await self.read_unique_task(id)

        if task.concluded:
            task.concluded = False
        else:
            task.concluded = True

        self.db.add(task)
        self.db.commit()

        return task


    async def delete_task(self, id: int):
        task = await self.read_unique_task(id)

        self.db.delete(task)
        self.db.commit()



    