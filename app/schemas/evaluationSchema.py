from pydantic import BaseModel, Field
from app.schemas.operationSchema import ReadOperationSchema
from app.enum.tradeEnum import EmotionalsEnum

class ReadEvaluationSchema(BaseModel):
    id: int
    emotional: EmotionalsEnum
    reason_for_entry: str
    rules_respected: bool
    committed_error: str | None
    operations: ReadOperationSchema

    model_config = {
        "from_attributes": True
    }


class EvaluationSchema(BaseModel):
    emotional: EmotionalsEnum = Field(default=EmotionalsEnum.TRANQUILO)
    reason_for_entry: str 
    rules_respected: bool
    committed_error: str | None
    operation_id: int

    model_config = {
        "from_attributes": True
    }