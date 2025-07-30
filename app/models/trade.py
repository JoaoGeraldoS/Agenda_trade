from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Enum, func, String
from datetime import datetime
from app.core.dataBase import Base
from app.enum.tradeEnum import Order, StatusTrade, EmotionalsEnum
from typing import List

class Active(Base):
    __tablename__ = "actives"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    market: Mapped[str] = mapped_column(String(100) ,nullable=False)
    description: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    operations: Mapped[List["Operation"]] = relationship(back_populates="active")
    user: Mapped["User"] = relationship(back_populates="active")


class Operation(Base):
    __tablename__ = "operations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    operation_type: Mapped[str] = mapped_column(Enum(Order), nullable=False)
    operation_date: Mapped[datetime] = mapped_column(nullable=False, default=func.now())
    input_price: Mapped[float] = mapped_column(nullable=False)
    out_price: Mapped[float]
    quantity: Mapped[float] = mapped_column(nullable=False)
    profit_loss: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[str] = mapped_column(Enum(StatusTrade))
    active_id: Mapped[int] = mapped_column(ForeignKey("actives.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    active: Mapped["Active"] = relationship(back_populates="operations")
    user: Mapped["User"] = relationship(back_populates="operations")
    evaluation: Mapped["Evaluation"] = relationship(back_populates="operations")


class Evaluation(Base):
    __tablename__ = "evaluations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    emotional: Mapped[str] = mapped_column(Enum(EmotionalsEnum), default=EmotionalsEnum.TRANQUILO)
    reason_for_entry: Mapped[str] = mapped_column(nullable=False)
    rules_respected: Mapped[bool] = mapped_column(nullable=False)
    committed_error: Mapped[str]
    operation_id: Mapped[int] = mapped_column(ForeignKey("operations.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    operations: Mapped["Operation"] = relationship(back_populates="evaluation")
    user: Mapped["User"] = relationship(back_populates="evaluation")
