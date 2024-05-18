
from dataclasses import dataclass,field
from datetime import date
from typing import Optional
import itertools
import pytest
from typing import List
from datetime import timedelta
today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)

# some design problems:
# 1) autoincrement the id, if you autoincrement, save last known for startup
# 2) correlate w/db. have db create pk then read from db
# 3) integrity check on id, if you create it make sure there are no holes
# else DB responsibility. Built into db autoincrement index. Guaranteed to be atomic
# thread safe and fault tolerant in DB. 
# 4) microservice, need lock for shared state. db has locks, you dont see them
# 

#not frozen
#Batch is the database put/get
class Batch:
    def __init__(self, batch_id:str, sku:str, qty:int, eta:Optional[date]):
        self.reference=batch_id
        self.sku =sku;
        self.available_quantity=qty
        self.eta = eta
        self.allocated_orderlines=[]
    def __eq__(self, other):
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference
    def __hash__(self):
        return hash(self.reference)
    def __gt__(self,other):
        if self.eta is None:
            return False
        if other.eta is None:
            return True
        return self.eta > other.eta
    
    def allocate(self,orderLine):
        #print("calling batch allocate orderLine:",orderLine)
        if self.can_allocate(orderLine)==True:
            self.available_quantity -=orderLine.qty
            self.allocated_orderlines.append(orderLine)
        
    def can_allocate(self,orderLine):
        #print("calling batch can_allocate orderLine:",orderLine,self.reference)
        if orderLine.qty>self.available_quantity or orderLine.sku!=self.sku or self.search(orderLine)==True:
            return False
        return True
    #to unwind an orderline transaction
    #why do we need the search statement to be true? to guard vs exception if item not in list
    def deallocate(self,orderLine):
        if self.search(orderLine):
            self.allocated_orderlines.remove(orderLine)

        
    def search(self,orderLine):
        for x in self.allocated_orderlines:
            if x==orderLine:
                return True
        return False

def test_batch_methods():
    # test equal
    sku="random_sku"
    batch_qty=10
    b1 = Batch("batch-001", sku, batch_qty, eta=date.today())
    b_old = Batch("batch-001", sku, batch_qty, eta=date.yesterday())
    print(b1==b_old)

# be careful with immutable objects. Assumption is it is magically good. only good for somethings
# good for copy in python, good for thread safety which implies safe for microservice
# bad in there is no equivalent pattern in db schema/storage. This is persistent safe. Not fault tolerant 
#
@dataclass(frozen=True)
class OrderLine:
    orderName : str
    sku : str
    qty : int

def allocate(line: OrderLine, batches: List[Batch]) -> str:
    try:
        batch = next(b for b in sorted(batches) if b.can_allocate(line))
        batch.allocate(line)
        return batch.reference
    except StopIteration:
        raise OutOfStock(f"Out of stock for sku {line.sku}")

class Product:
    sku:str

class OutOfStock(Exception):
    pass

class Customer:
    cust_name:str
    def place_order(sku, quantity):
        #how to generate an orderref? 
        return Order(str(quantity)+" units of "+sku,sku, quantity)
        
#this is mutable
@dataclass(unsafe_hash=True)
class Order:
    order_reference:str
    orderLines:List['Order'] = field(default_factory=list, init=False, compare=False, hash=False)

def test_value_class_order():
    o1= Order("o1_ref")
    o2= Order("o1_ref")
    o3= Order("ssss")
    o2.orderLines.append(OrderLine("ol","sku",100))
    #print("o1:",o1)
    #print("o2:",o2)
    #print("o1==o2:",o1==o2)
    assert o1==o1,"o1 not equal to itself"
    assert o1==o2,"o1 should not be equal to o2 because of list"
    assert o1!=o3,"o1 not equal to o3"
    
    
    

def test_value_class_OrderLine():
    pass
    

def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch("batch-001", sku, batch_qty, eta=date.today()),
        OrderLine("order-123", sku, line_qty)
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine('order-ref', "SMALL-TABLE", 2)
    batch.allocate(line)

    assert batch.available_quantity == 18
    
def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT-LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)

def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = make_batch_and_line("ELEGANT-LAMP", 2, 20)
    assert small_batch.can_allocate(large_line) is False

def test_can_allocate_if_available_equal_to_required():
    batch, line = make_batch_and_line("ELEGANT-LAMP", 2, 2)
    assert batch.can_allocate(line)

def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    different_sku_line = OrderLine("order-123", "EXPENSIVE-TOASTER", 10)
    assert batch.can_allocate(different_sku_line) is False

def test_search_orderline():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    ol1 = OrderLine("order_test1","UNCOMFORTABLE-CHAIR", 1)
    batch.allocate(ol1)
    assert batch.search(ol1) is True

def test_deallocate():
    batch = Batch("batch-001", "UNCOMFORTABLE-CHAIR", 100, eta=None)
    ol1 = OrderLine("order_test1","UNCOMFORTABLE-CHAIR", 1)
    batch.allocate(ol1)
    batch.deallocate(ol1)
    assert(len(batch.allocated_orderlines)==0)
    #we should test if something not there
    batch.deallocate(ol1)

#this is kind of a funny interface. Batch is created by someone which orders inventory. 
#
#it is really a set? all of these are unique? Doesnt make sense
def test_allocation_is_idempotent():
    batch, line = make_batch_and_line("ANGULAR-DESK", 20, 2)
    batch.allocate(line)
    batch.allocate(line)
    assert batch.available_quantity == 18
    
def test_prefers_current_stock_batches_to_shipments():
    in_stock_batch = Batch("in-stock-batch", "RETRO-CLOCK", 100, eta=None)
    shipment_batch = Batch("shipment-batch", "RETRO-CLOCK", 100, eta=tomorrow)
    line = OrderLine("oref", "RETRO-CLOCK", 10)

    allocate(line, [in_stock_batch, shipment_batch])
    assert in_stock_batch.available_quantity == 90
    assert shipment_batch.available_quantity == 100


def test_prefers_earlier_batches():
    earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
    medium = Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
    latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)
    line = OrderLine("order1", "MINIMALIST-SPOON", 10)

    allocate(line, [medium, earliest, latest])
    #print("test_prefers_earlier_batches:",earliest.available_quantity,medium.available_quantity,latest.available_quantity)

    assert earliest.available_quantity == 90
    assert medium.available_quantity == 100
    assert latest.available_quantity == 100


def test_returns_allocated_batch_ref():
    in_stock_batch = Batch("in-stock-batch-ref", "HIGHBROW-POSTER", 100, eta=None)
    shipment_batch = Batch("shipment-batch-ref", "HIGHBROW-POSTER", 100, eta=tomorrow)
    line = OrderLine("oref", "HIGHBROW-POSTER", 10)
    allocation = allocate(line, [in_stock_batch, shipment_batch])
    #print("test_returns_allocated_batch_ref:",allocation,in_stock_batch.reference)
    assert allocation == in_stock_batch.reference



def test_prefers_warehouse_batches_to_shipments():
  print("allocate warehouse batch first before shipment batch")
  


def test_Batch_hash():
  earliest = Batch("speedy-batch", "MINIMALIST-SPOON", 100, eta=today)
  medium = Batch("normal-batch", "MINIMALIST-SPOON", 100, eta=tomorrow)
  latest = Batch("slow-batch", "MINIMALIST-SPOON", 100, eta=later)
  dict_batch={}
  dict_batch[earliest] = 1
  dict_batch[medium] = 2
  dict_batch[latest] = 3
  print("earliest value:",dict_batch[earliest],dict_batch[medium],dict_batch[latest])
  list_batch=[earliest, latest,medium]
  print(list_batch)
  print(sorted(list_batch))
  print(hash(earliest),hash(medium),hash(latest))
  
test_value_class_order()
test_allocating_to_a_batch_reduces_the_available_quantity()
test_can_allocate_if_available_greater_than_required()
test_cannot_allocate_if_available_smaller_than_required()
test_can_allocate_if_available_equal_to_required()
test_cannot_allocate_if_skus_do_not_match()
test_deallocate()
test_search_orderline()
test_allocation_is_idempotent()
test_prefers_current_stock_batches_to_shipments()
#test_Batch_hash()
test_prefers_earlier_batches()
test_returns_allocated_batch_ref()