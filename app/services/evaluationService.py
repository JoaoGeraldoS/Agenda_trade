from app.schemas.evaluationSchema import EvaluationSchema, ReadEvaluationSchema
from app.repositories.evaluationRepository import EvaluationRepository


class EvaluationService:
    def __init__(self, evalu_repo: EvaluationRepository):
        self.evalu_repo = evalu_repo

    
    def read_evaluation_service(self, user_id: int) -> list[ReadEvaluationSchema]:
        return self.evalu_repo.read_evaluation(user_id=user_id)
    
    
    def read_by_id_service(self, id: int, user_id: int) -> ReadEvaluationSchema:
        return self.evalu_repo.read_by_id(id=id, user_id=user_id)
    
    
    def create_evaluation_service(self, eval_schema: EvaluationSchema, user_id) -> ReadEvaluationSchema:
        evaluation = self.evalu_repo.create_evaluation(evalu=eval_schema, user_id=user_id)
        self.evalu_repo.db.commit()

        return ReadEvaluationSchema.model_validate(evaluation)
        