from pydantic import BaseModel
from app.schemas.users.user_schema import UserNameSchema


class ReadActiveSchema(BaseModel):
    id: int
    name: str
    market: str
    decription: str
    user: UserNameSchema
    

    model_config = {
        "from_attributes": True
    }


class ActiveSchema(BaseModel):
    name: str
    market: str
    decription: str | None = None

    model_config = {
        "from_attributes": True
    }