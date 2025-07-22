from app.schemas.operationSchema import OperationSchema
from app.enum.tradeEnum import Order
from decimal import Decimal, getcontext

def get_total_profit(operation: OperationSchema, name: str, contract_size: int = 100000) -> Decimal:
   
    getcontext().prec = 10

    in_price = Decimal(str(operation.input_price))
    out_price = Decimal(str(operation.out_price))
    lot = Decimal(str(operation.quantity))  

    
    pair_symbol = name.upper()

    print(pair_symbol)
    
    if "JPY" in pair_symbol:
        pip_size = Decimal("0.01")
    else:
        pip_size = Decimal("0.0001")

    
    if operation.operation_type == Order.BUY:
        pip_diff = (out_price - in_price) / pip_size
    else:
        pip_diff = (in_price - out_price) / pip_size

    
    profit = pip_diff * pip_size * lot * contract_size
    return profit



