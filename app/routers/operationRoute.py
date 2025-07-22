from fastapi import APIRouter, Depends, status
from app.schemas.operationSchema import ReadOperationSchema, OperationSchema
from app.dependencies.service import get_op_service
from app.dependencies.verify_token import verify_token
from app.services.operation_service import OperationService
from app.enum.tradeEnum import Order

router = APIRouter(prefix="/operation", tags=["Operation"])

@router.get("/", response_model=list[ReadOperationSchema], status_code=status.HTTP_200_OK)
async def read_all_operations(op_service: OperationService = Depends(get_op_service), token: verify_token = Depends()):
    return op_service.read_operation_service(user_id=token.id)


@router.get("/{id}", response_model=ReadOperationSchema, status_code=status.HTTP_200_OK) 
async def read_byId_operation(id: int, op_service: OperationService = Depends(get_op_service), token: verify_token = Depends()):
    return op_service.read_operation_byId_service(id=id, user_id=token.id)


@router.post("/", response_model=ReadOperationSchema, status_code=status.HTTP_201_CREATED)
async def create_operation(
    op_schema: OperationSchema,
    op_service: OperationService = Depends(get_op_service),
    token: verify_token = Depends()):

    
    return op_service.create_operation_service(op_schema, user_id=token.id)


@router.patch("/{id}", response_model=ReadOperationSchema, status_code=status.HTTP_200_OK)
async def update_operation(
    id: int,
    op_schema: OperationSchema,
    op_service: OperationService = Depends(get_op_service),
    token: verify_token = Depends()):

    return op_service.update_operation_service(id=id, operation_schema=op_schema, user_id=token.id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_operation(id: int,op_service: OperationService = Depends(get_op_service),token: verify_token = Depends()):
    return op_service.delete_operation_service(id=id, user_id=token.id)

