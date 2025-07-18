from app.models.base import Base
from sqlalchemy import String, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from enum import Enum as PyEnum
from typing import List
from datetime import datetime

class Active(Base):
    __tablename__ = "actives"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    market: Mapped[str] = mapped_column(String(100) ,nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    operations: Mapped[List["Operation"]] = relationship(back_populates="active")
    user: Mapped["User"] = relationship(back_populates="active")


class Order(PyEnum):
    BUY = "BUY"
    SELL = "SELL"

class StatusTrade(PyEnum):
    ABERTA = "ABERTA"
    FECHADA = "FECHADA"


class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    operation_type: Mapped[str] = mapped_column(SqlEnum(Order), nullable=False)
    operation_date: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    input_price: Mapped[float] = mapped_column(nullable=False)
    out_price: Mapped[float]
    quantity: Mapped[float] = mapped_column(nullable=False)
    profit_loss: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(SqlEnum(StatusTrade))
    active_id: Mapped[int] = mapped_column(ForeignKey("actives.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    active: Mapped["Active"] = relationship(back_populates="operations")
    user: Mapped["User"] = relationship(back_populates="operations")






