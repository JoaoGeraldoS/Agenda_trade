from enum import Enum

class Order(Enum):
    BUY = "BUY"
    SELL = "SELL"

class StatusTrade(Enum):
    ABERTA = "ABERTA"
    FECHADA = "FECHADA"