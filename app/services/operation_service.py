from app.repositories.operationRepository import OperationRepository
from app.schemas.operationSchema import ReadOperationSchema, OperationSchema
from app.exceptions.generic_exeption import NotFound, BadRequest
from app.enum.tradeEnum import StatusTrade
from app.utils.get_total_profit import get_total_profit
from decimal import Decimal


class OperationService:
    def __init__(self, operation_repo: OperationRepository):
        self.operation_repo = operation_repo
        


    def read_operation_service(self, user_id: int) -> list[ReadOperationSchema]:
        return self.operation_repo.read_operation(user_id=user_id)
    
    
    def read_operation_byId_service(self, id: int, user_id: int) -> ReadOperationSchema:
        operation_id = self.operation_repo.read_by_id(id=id, user_id=user_id)

        if operation_id is None:
            raise NotFound("Operação inesistente")

        return ReadOperationSchema.model_validate(operation_id)
    

    def create_operation_service(self, operation_schema: OperationSchema, user_id: int) -> ReadOperationSchema:
        active = self.operation_repo.read_byId_active(operation_schema.active_id, user_id)

        if operation_schema.input_price <= 0:
            raise BadRequest("O preço deve ser maior que 0")
        
        if operation_schema.quantity <= 0:
            raise BadRequest("A quantidade deve ser maior que 0")
        
        if operation_schema.out_price:
            operation_schema.status = StatusTrade.FECHADA

            profit = get_total_profit(operation=operation_schema, name=active.name)

        new_operation = self.operation_repo.create_operation(operation_schema, user_id=user_id, value_profit=profit)

        self.operation_repo.db.commit()
        return ReadOperationSchema.model_validate(new_operation)
    

    def update_operation_service(self,id: int, operation_schema: OperationSchema, user_id: int) -> ReadOperationSchema:
        operation_byId = self.operation_repo.read_by_id(id=id, user_id=user_id)
        active = self.operation_repo.read_byId_active(operation_schema.active_id, user_id)

        if operation_byId is None:
            raise NotFound("Operação inesistente")
        
        
        if operation_schema.out_price:
            operation_schema.status = StatusTrade.FECHADA

            profit = get_total_profit(operation=operation_schema, name=active.name)


        update_operation = self.operation_repo.update_operation(id=id, operation_schema=operation_schema, user_id=user_id, value_profit=profit)
        self.operation_repo.db.commit()
       
        return ReadOperationSchema.model_validate(update_operation)
    

    def delete_operation_service(self, id: int, user_id: int) -> None:
        operation_byId = self.operation_repo.read_by_id(id=id, user_id=user_id)

        if operation_byId is None:
            raise NotFound("Operação inesistente")
        
        self.operation_repo.delete_operation(operation_byId.id)
        self.operation_repo.db.commit()