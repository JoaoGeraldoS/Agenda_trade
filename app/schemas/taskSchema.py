from pydantic import BaseModel, Field
from datetime import datetime

from app.schemas.usersSchema import UserNameSchema


class ReadTaskSchema(BaseModel):
    id: int
    title: str
    description: str 
    created_at: datetime
    concluded: bool
    user: UserNameSchema

    model_config = {
        "from_attributes": True
    }

class CreateTaskSchema(BaseModel):
    title: str
    description: str | None = None
    concluded: bool = Field(default=False) 


    model_config = {
        "from_attributes": True
    }
