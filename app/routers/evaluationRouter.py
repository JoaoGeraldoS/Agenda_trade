from fastapi import APIRouter, Depends, status
from app.schemas.evaluationSchema import ReadEvaluationSchema, EvaluationSchema
from app.services.evaluationService import EvaluationService
from app.dependencies.service import get_eval_service
from app.dependencies.verify_token import verify_token


router = APIRouter(prefix="/evaluation", tags=["Evaluation"])

@router.get("/", response_model=list[ReadEvaluationSchema], status_code=status.HTTP_200_OK)
async def read_evaluation(
    eval_service: EvaluationService = Depends(get_eval_service),
    token: verify_token = Depends()):

    return eval_service.read_evaluation_service(token.id)


@router.get("/{id}", response_model=ReadEvaluationSchema, status_code=status.HTTP_200_OK)
async def read_by_id(
    id: int,
    eval_service: EvaluationService = Depends(get_eval_service),
    token: verify_token = Depends()):

    return eval_service.read_by_id_service(id=id, user_id=token.id)


@router.post("/", response_model=ReadEvaluationSchema, status_code=status.HTTP_201_CREATED)
async def create_evaluation(
    eval_schema: EvaluationSchema,
    eval_service: EvaluationService = Depends(get_eval_service),
    token: verify_token = Depends()):

    return eval_service.create_evaluation_service(eval_schema=eval_schema, user_id=token.id)

