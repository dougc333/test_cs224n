from abc import ABC, abstractmethod



class BillingStrategy(ABC):
    @abstractmethod
    def get_act_price(self,raw_price:float)-> None:
        raise NotImplementedError

class NormalStrategy(BillingStrategy):
    def get_act_price(self, raw_price: float) -> float:
        return raw_price

class HappyHourStrategy(BillingStrategy):
    def get_act_price(self, raw_price: float) -> float:
        return raw_price * 0.5

#modification 1) change __str__ to string return
#add get_total method
class Bill:
    def __init__(self, billingStrategy:BillingStrategy):
        self.drinks:list[float] = []
        self._billing_strategy = billingStrategy
    
    @property
    def billing_strategy(self)->BillingStrategy:
        print("getter")
        return self._billing_strategy
    
    @billing_strategy.setter
    def billing_strategy(self, billing_strategy:BillingStrategy) -> None:
        print("setter")
        self._billing_strategy = billing_strategy

    def add(self,price:float, quantity:int) ->None:
        self.drinks.append(self.billing_strategy.get_act_price(price * quantity))
    
    def __str__(self):
        return str(f"bill self.drinks:{self.drinks} total:{self.get_total()}")

    def get_total(self)->float:
        return sum(self.drinks)

def verify_totals():



def main()->None:
    normal_strategy = NormalStrategy()
    happy_hour_strategy = HappyHourStrategy()
    #why are there 2 places to set strategy? 
    #one in the Bill ctor and another in instance? 
    customer_1 = Bill(normal_strategy)
    customer_2 = Bill(normal_strategy)

    customer_1.add(2.50,3)
    customer_1.add(2.50,2)

    customer_1.billing_strategy = happy_hour_strategy
    customer_2.billing_strategy = happy_hour_strategy
    customer_1.add(3.40,6)
    customer_2.add(3.10,2)

    customer_1.billing_strategy = normal_strategy
    customer_2.billing_strategy = normal_strategy

    customer_1.add(3.00,12)
    customer_2.add(1.00,1)

    print(f'customer1: {customer_1}, total:{customer_1.get_total()}')
    print(f"customer_2: {customer_2}, total:{customer_2.get_total()}")

if __name__=='__main__':
    main()