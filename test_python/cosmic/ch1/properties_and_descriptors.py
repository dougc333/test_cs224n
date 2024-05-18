#properties on functions intance variables
#properties are descriptors; descriptors can be used for ORM in python3 docs
#descriptors used for properties, static, super(), class methods
#

class OrderLine:
    reference:str
    sku:str
    qty:int


class TestBatch:
    def __init__(self,ref:str,sku:str,amt:int):
        self.reference = ref
        self.sku = sku
        self.available_qty = amt
        list_orderlines=List[OrderLine]=field(default_factor=list)
    def allocate(self,line:OrderLine):
        pass