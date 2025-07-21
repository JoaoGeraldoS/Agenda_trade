from pydantic import BaseModel
from app.schemas.usersSchema import UserNameSchema


class ReadActiveSchema(BaseModel):
    id: int
    name: str
    market: str
    description: str
    user: UserNameSchema
    

    model_config = {
        "from_attributes": True
    }


class ActiveSchema(BaseModel):
    name: str
    market: str
    description: str | None = None
   

    model_config = {
        "from_attributes": True
    }