from app.repositories.activeRepository import ActiveRepository
from app.schemas.activeSchema import ActiveSchema, ReadActiveSchema
from app.exceptions.generic_exeption import NotFound
from app.exceptions.active import ActiveExists


class ActiveService:
    def __init__(self, active_repo: ActiveRepository):
        self.active_repo = active_repo

    
    def read_all_active_service(self, user_id) -> list[ReadActiveSchema]:
        return self.active_repo.read_all_active(user_id=user_id)
    

    def read_active_id_service(self, id: int, user_id: int) -> ReadActiveSchema:
        active = self.active_repo.read_active_by_id(id=id, user_id=user_id)

        if not active:
            raise NotFound("Ativo não existente")
        
        return ReadActiveSchema.model_validate(active)
    

    def create_active_service(self, active_schema: ActiveSchema, user_id: int) -> ReadActiveSchema:
        active = self.active_repo.get_by_name(active_schema.name, user_id=user_id)

        if active:
            raise ActiveExists("Ativo já existente")
        
        create_active = self.active_repo.create_active(active_schema, user_id)
        self.active_repo.db.commit()
        return ReadActiveSchema.model_validate(create_active)
    

    def delete_active(self, id: int, user_id: int) -> None:
        active_by_id = self.active_repo.read_active_by_id(id=id, user_id=user_id)

        if not active_by_id:
            raise NotFound("Ativo não encontrado")
        
        self.active_repo.delete_active(active_by_id.id)
        self.active_repo.db.commit()
        
