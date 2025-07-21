from sqlalchemy.orm import Session
from sqlalchemy import select, delete

from app.models.trade import Active
from app.models.users import User
from app.schemas.activeSchema import ActiveSchema


class ActiveRepository:
    def __init__(self, db: Session):
        self.db = db

    def read_all_active(self, user_id: int) -> list[Active]:
        actives = self.db.execute(select(Active).join(User, User.id == Active.user_id).filter(User.id == user_id))
        return actives.scalars().all()
    

    def read_active_by_id(self, id: int, user_id: int) -> Active | None:
        active = self.db.execute(
            select(Active)
            .where(Active.id == id)
            .join(User, User.id == user_id)
            .filter(User.id == user_id)
        ).scalars().one_or_none()

        return active
    
    def get_by_name(self, name: str, user_id: int) -> Active | None:
        active = self.db.execute(
            select(Active)
            .where(Active.name == name)
            .join(User, User.id == Active.user_id)
            .filter(User.id == user_id)
        ).scalars().one_or_none()

        return active
    

    def create_active(self, active_schema: ActiveSchema, user_id) -> Active:
        active_data = active_schema.model_dump()

        active_data["user_id"] = user_id

        new_active = Active(**active_data)
        self.db.add(new_active)
        self.db.flush()
        self.db.refresh(new_active)
        return new_active
    

    def delete_active(self, id: int) -> None:
        self.db.execute(
            delete(Active)
            .where(Active.id == id)
        )
        self.db.flush()
    
