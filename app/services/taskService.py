from app.repositories.taskRepository import TaskRepository
from app.schemas.taskSchema import CreateTaskSchema, ReadTaskSchema
from app.exceptions.generic_exeption import NotFound

class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo


    def create_task_service(self, task_schema: CreateTaskSchema, user_id: int) -> ReadTaskSchema:
        create_task = self.task_repo.create_task(task_schema, user_id)
        self.task_repo.db.commit()
        return ReadTaskSchema.model_validate(create_task)


    def read_task_service(self, user_id: int) -> list[ReadTaskSchema]:
        return self.task_repo.read_task(user_id)
    

    def read_task_by_id_service(self, id: int, user_id: int) -> ReadTaskSchema:
        task_by_id = self.task_repo.read_by_id(id, user_id)

        if not task_by_id:
            raise NotFound("Tarefa não encontrada")
        
        return ReadTaskSchema.model_validate(task_by_id)


    def update_task_service(self, task_schema: CreateTaskSchema, id: int, user_id: int) -> ReadTaskSchema:
        task_by_id = self.task_repo.read_by_id(id, user_id)

        if not task_by_id:
            raise NotFound("Tarefa não encontrada")
        
        task_update = self.task_repo.update_task(task_schema, id, user_id)
        self.task_repo.db.commit()

        return ReadTaskSchema.model_validate(task_update)
    

    def update_task_concluded_service(self, id: int, user_id: int) -> ReadTaskSchema:
        task_by_id = self.task_repo.read_by_id(id, user_id)
        
        if not task_by_id:
            raise NotFound("Tarefa não encontrada")
        
        if task_by_id.concluded:
            task_by_id.concluded = False
        else:
            task_by_id.concluded = True
        
        update_concluded = self.task_repo.update_concluded(task_by_id)
        self.task_repo.db.commit()

        return ReadTaskSchema.model_validate(update_concluded)

    
    def delete_task_service(self, id: int, user_id) -> None:
        task_by_id = self.task_repo.read_by_id(id, user_id)

        if not task_by_id:
            raise NotFound("Tarefa não encontrada")
        
        self.task_repo.delete_task(id)
        self.task_repo.db.commit()
       
