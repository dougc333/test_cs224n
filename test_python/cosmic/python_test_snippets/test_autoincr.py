import itertools

class Product:
    newid=itertools.count()
    def __init__(self):
        self.id=next(Product.newid)
        print("self.id:",self.id)
    
p=Product()
p1=Product()
print("p:",p)
print("p1:",p1)
