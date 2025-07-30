from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.dataBase import Base
from typing import List

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    hash_password: Mapped[str] = mapped_column(nullable=False)

    task: Mapped[List["Task"]] = relationship(back_populates="user")
    active: Mapped[List["Active"]] = relationship(back_populates="user")
    operations: Mapped[List["Operation"]] = relationship(back_populates="user")
    evaluation: Mapped["Evaluation"] = relationship(back_populates="user")
