#using context manager pattern 
#none of tehse 2 versions is good enough for production 

from typing import List


class PoolManager:
    def __init__(self, pool):
        self.pool = pool

    def __enter__(self):
        self.obj = self.pool.acquire()
        return self.obj
    
    def __exit__(self):
        self.pool.release(self.obj)
    
class Reusable:
    def test(self):
        print(f"using object id({self})")

class ReusablePool(Reusable):
    def __init__(self,size):
        self.size = size
        self.free : List[Reusable]
        self.in_use : List[Reusable]
