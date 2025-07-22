from pydantic import BaseModel, Field
from datetime import datetime
from app.enum.tradeEnum import StatusTrade, Order
from app.schemas.activeSchema import ActiveOperation
from app.schemas.usersSchema import UserNameSchema
from zoneinfo import ZoneInfo

class ReadOperationSchema(BaseModel):
    id: int
    operation_type: Order
    operation_date: datetime
    input_price: float
    out_price: float
    quantity: float
    profit_loss: float
    status: StatusTrade
    active: ActiveOperation
    user: UserNameSchema


    model_config = {
        "from_attributes": True,
        "json_encoders": {
            datetime: lambda v:(
                v.replace(tzinfo=ZoneInfo("UTC")) if v.tzinfo is None else v
            ).astimezone(ZoneInfo("America/Sao_Paulo")).strftime("%d/%m/%Y")
        }
    }


class OperationSchema(BaseModel):
    operation_type: Order = Field(example="BUY")
    input_price: float
    out_price: float | None = None
    quantity: float
    status: StatusTrade = Field(example="ABERTA")
    active_id: int

    model_config = {
        "from_attributes": True,
        
    }

