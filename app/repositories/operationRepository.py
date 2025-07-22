from sqlalchemy.orm import Session
from sqlalchemy import select, delete, update
from decimal import Decimal

from app.models.trade import Operation
from app.models.users import User
from app.models.trade import Active
from app.schemas.operationSchema import OperationSchema
from app.models.trade import Active


class OperationRepository:
    def __init__(self, db: Session):
        self.db = db

    
    def read_operation(self, user_id: int) -> list[Operation]:
        operations = self.db.execute(
            select(Operation)
            .join(User, User.id == Operation.user_id)
            .join(Active, Active.id == Operation.active_id)
            .filter(User.id == user_id)
        )
        return operations.scalars().all()
    
    
    def read_by_id(self, id: int, user_id: int) -> Operation:
        operation = self.db.execute(
            select(Operation)
            .where(Operation.id == id)
            .join(User, User.id == Operation.user_id)
            .join(Active, Active.id == Operation.active_id)
            .filter(User.id == user_id)
        ).scalars().one_or_none()

        return operation
    
    def read_byId_active(self, id: int, user_id: int):
        active = self.db.execute(
            select(Active)
            .where(Active.id == id)
            .join(User, User.id == Active.user_id)
            .filter(User.id == user_id)
        ).scalars().one_or_none()

        return active
    
    
    def create_operation(self, operation_schema: OperationSchema, user_id: int, value_profit: Decimal) -> Operation:
        operation_data = operation_schema.model_dump()

        operation_data["user_id"] = user_id
        operation_data["profit_loss"] = value_profit

        new_operation = Operation(**operation_data)
        self.db.add(new_operation)
        self.db.flush()
        self.db.refresh(new_operation)

        return new_operation
      

    def update_operation(self,id: int, operation_schema: OperationSchema, user_id: int, value_profit: Decimal) -> Operation | None:
        update_data = operation_schema.model_dump(exclude_unset=True)
        update_data["profit_loss"] = value_profit

        rows_affected = self.db.execute(
            update(Operation)
            .where(Operation.id == id)
            .values(**update_data)
        ).rowcount

        self.db.flush()

        if not rows_affected:
            return None
        
        return self.read_by_id(id=id, user_id=user_id)
    

    def delete_operation(self, id: int) -> None:
        self.db.execute(
            delete(Operation)
            .where(Operation.id == id)
        )
        self.db.flush()