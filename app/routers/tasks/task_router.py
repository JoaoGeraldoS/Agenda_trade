from fastapi import Depends, status, APIRouter
from app.schemas.tasks.task_schema import ReadTaskSchema, CreateTaskSchema
from app.services.tasks.task_service import TaskService
from typing import List
from app.dependencies import verify_token

router = APIRouter(prefix="/task", tags=["Tasks"])


@router.get("/", response_model=List[ReadTaskSchema])
async def read_task(task_service: TaskService = Depends(), token: verify_token = Depends()):
    """
    Essa rota faz leitura de todas as tarefas no banco de dados e retorna um json com 
    elas em formato de listas, com o retorno de 200_ok
    """
    return await task_service.read_task(token.id)


@router.get("/{id}", response_model=ReadTaskSchema)
async def read_task_id(id: int, task_service: TaskService = Depends(), token: verify_token = Depends()):
    """
    Essa rota faz a leitura de apenas uma tarefa passada pelo id, e retorna um json com ela com o retorno de 200_ok.
    Se a tarefa não existir, tera um retorno 404_not_found
    """
    return await task_service.read_unique_task(id, token.id)


@router.post("/", response_model=ReadTaskSchema, status_code=status.HTTP_201_CREATED)
async def create_task(task_schema: CreateTaskSchema, task_service: TaskService = Depends(), token: verify_token = Depends()):
    """
    Essa rota cria a tarefa, ela recebe um json como "Titulo, Descrição, Concluida", O campo Concluida é passada automaticamente
    como falso, ao ser salvo, terá um retorno 201_created e os dados criados via json, na criação o usuario será passado automaticamante. 
    """
    return await task_service.create_task(task_schema, token.id)


@router.put("/{id}", response_model=ReadTaskSchema)
async def update_task(id: int, task_schema: CreateTaskSchema, task_service: TaskService = Depends(), token: verify_token = Depends()):
    """
    Essa rota faz a atualização da tarefa passada pelo id, se não existir, tera um retorno 404_not_found.
    Ela usa o mesmo json da rota de criação "Titulo, Descrição, Concluida", aqui pode ser editado todos os campos.
    Será retornado um 200_ok e um json com os campos editados.
    """
    return await task_service.update_task(id, task_schema)


@router.patch("/{id}/concluded", response_model=ReadTaskSchema)
async def update_concluded(id: int, task_service: TaskService = Depends(), token: verify_token = Depends()):
    """
    Essa rota faz a atualização do campo "Concluida", basta passar o id da tarefa, se ela não existir, tera um retorno 404_not_found.
    Se ela existir tera o retorno do json com todos os dados da tarefa e uma retorno 200_ok.
    """
    return await task_service.update_concluded(id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(id: int, task_service: TaskService = Depends(), token: verify_token = Depends()):
    """
    Essa rota apaga uma tarefa passada pelo id, se não existir, tera um retorno 404_not_found.
    Se ela exitir terá um retorno vazio "sem conteudo" 204_no_content
    """
    return await task_service.delete_task(id)