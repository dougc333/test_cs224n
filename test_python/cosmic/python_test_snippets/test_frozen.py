
from dataclasses import dataclass


class Obj:
   def __init__(self) -> None:
       pass    
o=Obj()
#oh....
print("id and hash o:",id(o)/16,hash(o))

        

#@dataclass(frozen=True) 
class OrderLineFrozen:
   pass
    
#ol=OrderLineFrozen('order-ref', "SMALL-TABLE", 2)
ol=OrderLineFrozen()
print("do you see __hash__ for frozen? ol:",dir(ol))
print("hash ol:",hash(ol))
print("id,hash ol:",id(ol),id(ol)/16)

@dataclass(unsafe_hash=False)
class OrderLineUnsafeHash:
    ref:str
    sku:str
    qty:int

o1=OrderLineUnsafeHash("o1","SMALL_CHAIR",10)
print("  ")
#cant have unsafe_hash=False for OrderLineUnsafeHash. means no hash function
print("do you see __hash__ with unsafe hash? o1:",dir(o1))
print("hash o1:",hash(o1))