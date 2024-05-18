
from abc import ABC, abstractmethod
from dataclasses import dataclass,field

class BillingStrategy(ABC):
   @abstractmethod
   def get_price(self)-> float:
       pass

@dataclass
class MenuItem(ABC):
   name:str = ""
   price:float = 0.0
   quantity:int = 0
   bill_strategy:BillingStrategy = None

   def get_price_menu_item(self)-> float:
       return self.bill_strategy.get_price(self.price)


class NormalBillingStrategy(BillingStrategy):
    def get_price(self,price:float)-> float:
        return price

class HappyHourBillingStrategy(BillingStrategy):
    def get_price(self,price:float)-> float:
        return 0.5 * price
    
@dataclass
class Bill:
    customer_name:str = ""
    ordered_items: list[MenuItem] = field(default_factory=list)

    def get_bill_total(self)-> float:
        return sum(self.ordered_items)

    def add_item(self,food_item:MenuItem):
        self.ordered_items.append(food_item)
    
    def get_bill_total(self)-> float:
        total = 0.
        for menu_item in self.ordered_items:
            total += menu_item.get_price_menu_item()
        return total

def main()->None:
    bobs_bill = Bill("bob")
    bobs_bill.add_item(MenuItem("fries", 4.50, 1, NormalBillingStrategy()))
    bobs_bill.add_item(MenuItem("burger", 14.50, 1, HappyHourBillingStrategy()))
    bobs_bill.add_item(MenuItem("shake", 5.50, 1, HappyHourBillingStrategy()))
    print("total:",bobs_bill.get_bill_total())
    assert  bobs_bill.get_bill_total() == 14.5

if __name__=="__main__":
    main()