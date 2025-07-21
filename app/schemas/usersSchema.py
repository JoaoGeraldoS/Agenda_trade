from pydantic import BaseModel

class UserSchema(BaseModel):
    id: int
    name: str
    username: str
    password: str

    model_config = {
        "from_attributes": True
    }

class CreateUserSchema(BaseModel):
    name: str
    username: str
    password: str

    model_config = {
        "from_attributes": True
    }

class ReturnUserSchema(BaseModel):
    name: str
    username: str
    
    model_config = {
        "from_attributes": True
    }

class LoginUserSchema(BaseModel):
    username: str
    password: str

    model_config = {
        "from_attributes": True
    }

class UserNameSchema(BaseModel):
    name: str

    model_config = {
        "from_attributes": True
    }