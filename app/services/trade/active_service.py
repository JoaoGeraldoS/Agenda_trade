from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from app.schemas.trade.active import ActiveSchema
from app.models.trade.active import Active
from app.models.user.user_model import User
from app.db.session import get_db
from app.errors import erros_exptions

class ActiveService:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    async def read_active(self, id: int):
        actives = self.db.execute(select(Active).join(User,User.id == Active.user_id).filter(User.id == id))
        return actives.scalars().all()
    
    async def read_unique_active(self, id: int, id_user: int):
        active = self.db.execute(select(Active)
                               .where(Active.id == id)
                               .join(User, User.id == Active.user_id)
                               .filter(User.id == id_user)).scalars().one_or_none()
        
        if active is None:
            raise erros_exptions.IsNotNoneException("Ativo não existe")
        
        return active

    async def create_active(self, active_schema: ActiveSchema, id: int):
        new_active = Active()

        