from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.tasks.task_model import Task
from ..base import Base
from typing import List

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    task: Mapped[List["Task"]] = relationship(back_populates="user") 