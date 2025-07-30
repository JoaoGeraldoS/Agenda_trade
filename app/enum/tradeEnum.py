from enum import Enum

class Order(Enum):
    BUY = "BUY"
    SELL = "SELL"

class StatusTrade(Enum):
    ABERTA = "ABERTA"
    FECHADA = "FECHADA"

class EmotionalsEnum(Enum):
    TRANQUILO = "TRANQUILO"
    ANCIOSO = "ANCIOSO"
    CONFIANTE = "CONFIANTE"
    DEPRESSIVO = "DEPRESSIVO"