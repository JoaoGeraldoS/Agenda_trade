from sqlalchemy.orm import Session
from sqlalchemy import select, update, delete

from app.models.tasks import Task
from app.models.users import User
from app.schemas.taskSchema import CreateTaskSchema

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db


    def read_task(self, id: int) -> list[Task]:
        tasks = self.db.execute(select(Task).join(User, User.id == Task.user_id).filter(User.id == id))
        return tasks.scalars().all()
    

    def read_by_id(self, id: int, id_user: int) -> Task | None:
        task = self.db.execute(
            select(Task)
            .where(Task.id == id)
            .join(User, User.id == Task.user_id)
            .filter(User.id == id_user)).scalars().one_or_none()

        return task
    

    def create_task(self, task_schema: CreateTaskSchema, user_id: int) -> Task:
        task_data = task_schema.model_dump()

        task_data["user_id"] = user_id 

        new_task = Task(**task_data)
        self.db.add(new_task)
        self.db.flush()
        self.db.refresh(new_task)
        return new_task
    

    def update_task(self, task_schema: CreateTaskSchema, task_id: int, user_id: int) -> Task | None:
        update_data = task_schema.model_dump(exclude_unset=True)

        rows_affected = self.db.execute(
            update(Task)
            .where(Task.id == task_id)
            .values(**update_data)).rowcount
        
        self.db.flush()
        
        if not rows_affected:
            return None
        
        return self.read_by_id(task_id, user_id)
    
    def update_concluded(self, task: Task) -> Task:
        self.db.add(task)
        self.db.flush()
        
        return task
    

    def delete_task(self, id: int) -> None:
        self.db.execute(
            delete(Task)
            .where(Task.id == id)
        )
        self.db.flush()