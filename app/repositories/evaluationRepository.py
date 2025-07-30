from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.trade import Evaluation
from app.models.users import User
from app.schemas.evaluationSchema import EvaluationSchema


class EvaluationRepository:
    def __init__(self, db: Session):
        self.db = db

    
    def read_evaluation(self,user_id: int) -> list[Evaluation]:
        evaluations = self.db.execute(
            select(Evaluation)
            .join(User, User.id == Evaluation.user_id)
            .filter(User.id == user_id)
        )

        return evaluations.scalars().all()
    

    def read_by_id(self, id: int, user_id: int) -> Evaluation:
        evaluation = self.db.execute(
            select(Evaluation)
            .where(Evaluation.id == id)
            .join(User, User.id == Evaluation.user_id)
            .filter(User.id == user_id)
        ).scalars().one_or_none()

        return evaluation
    

    def create_evaluation(self, evalu: EvaluationSchema, user_id: int) -> Evaluation:
        evaluation = evalu.model_dump()

        evaluation["user_id"] = user_id

        new_evaluation = Evaluation(**evaluation)
        self.db.add(new_evaluation)
        self.db.flush()
        self.db.refresh(new_evaluation)

        return new_evaluation
        


