from fastapi import APIRouter, Depends, status
from app.dependencies.verify_token import verify_token
from app.dependencies.service import get_active_service
from app.schemas.activeSchema import ActiveSchema, ReadActiveSchema
from app.services.activeService import ActiveService


router = APIRouter(prefix="/active", tags=["Active"])

@router.get("/", response_model=list[ReadActiveSchema], status_code=status.HTTP_200_OK)
async def read_actives(active_service: ActiveService = Depends(get_active_service), token: verify_token = Depends()):
    return active_service.read_all_active_service(token.id)


@router.get("/{id}", response_model=ReadActiveSchema, status_code=status.HTTP_200_OK)
async def read_active(id: int, active_service: ActiveService = Depends(get_active_service), token: verify_token = Depends()):
    return active_service.read_active_id_service(id=id, user_id=token.id)


@router.post("/", response_model=ReadActiveSchema, status_code=status.HTTP_201_CREATED)
async def create_active(
    active_schema: ActiveSchema,
    active_service: ActiveService = Depends(get_active_service),
    token: verify_token = Depends()):
    return active_service.create_active_service(active_schema=active_schema, user_id=token.id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_active(id: int, active_service: ActiveService = Depends(get_active_service), token: verify_token = Depends()):
    return active_service.delete_active(id=id, user_id=token.id)