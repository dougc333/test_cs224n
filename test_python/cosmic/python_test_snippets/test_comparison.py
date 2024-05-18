from dataclasses import dataclass


@dataclass(frozen=True)
class OrderLine:
    order_id : str
    sku : str
    qty : int
    stuff=[]

class Order:
    def __init__(self,a:str):
        self.a=a
        self.stuff=[]
    def __repr__(self):
        return self.a+","+str(len(self.stuff))
    
o1 = OrderLine("1","SMALL_TABLES",20)
o1.stuff.append("asdf")
o2 = OrderLine("1","SMALL_TABLES",20)

print(o1==o2)
print("o1:",o1)
print("o2:",o2)

or1 = Order("first_order")
or1.stuff.append("appending stuff to order 1")
print(or1)

or2 = Order("second_order")
print("or2:",or2)
print("or1==or2",or1==or2)