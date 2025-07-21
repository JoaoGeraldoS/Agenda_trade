from sqlalchemy.orm import Session
from sqlalchemy import select

from app.models.users import User
from app.schemas.usersSchema import CreateUserSchema

class UserRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_username(self, username: str) -> User | None:
        user_exist = self.db.execute(
            select(User)
            .where(User.username == username)
            ).scalars().one_or_none()
        
        return user_exist


    def create_user(self, user: CreateUserSchema) -> User:
        db_user = User(**user)
        self.db.add(db_user)
        self.db.flush()
        self.db.refresh(db_user)

        return db_user

        