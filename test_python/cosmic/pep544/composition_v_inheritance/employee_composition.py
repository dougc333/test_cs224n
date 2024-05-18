from abc import abstractmethod, ABC
from curses.ascii import EM
from dataclasses import dataclass
from typing import Optional
#https://www.youtube.com/watch?v=0mcP8ZpUR38&t=1056s
#is this really useful? There arent unit tests here
#the high level interfaces/ABC are Commission, Contract, Person
#

class Commission(ABC):
    """abstract base class Commission"""
    @abstractmethod
    def get_payment(self) -> float:
        '''calculate commission no impl here'''


@dataclass
class ContractCommission(Commission):
    '''Represents coommission'''
    commission: float = 100.
    contracts_landed: float = 0.
    
    def get_payment(self)->float:
        return self.commission * self.contracts_landed

class Contract(ABC):
    '''defines contract ABC'''
    @abstractmethod
    def get_payment(self) -> float:
        pass

@dataclass
class HourlyContract(Contract):
    pay_rate:float = 0.
    hours_worked:int = 0
    employer_cost:float = 0.
    
    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost
@dataclass
class SalariedContract(Contract):
    monthly_salary:float = 0.
    percentage:float = 1.
    
    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage 


@dataclass
class FreeLancerContract(Contract):
    pay_rate:float = 0.
    hours_worked:int = 0
    vat_number:str = ""
    
    def get_payment(self) -> float:
        return (self.pay_rate * self.hours_worked)
    
#this allows us to create other types of people besides employee
#also makes this look more like a value only class
@dataclass
class Person:
    name:str
    id:int

@dataclass
class Employee:
    personal_info: Person
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """compute pay for employee base class"""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout
    
@dataclass
class FreeLancer(Employee):
    contract:Contract
    commission:Optional[Commission] = None
        
def test_hourly_employee():
    henry_personal_info = Person(name="Henry", id=12)
    henry_contract = HourlyContract(pay_rate=10,hours_worked=10)
    henry = Employee(henry_personal_info, contract=henry_contract)
    
def main() -> None:
    henry_personal_info = Person(name="Henry", id=12)
    henry_contract = HourlyContract(pay_rate=10,hours_worked=10)
    henry = Employee(henry_personal_info, contract=henry_contract)
    print(
        f"HourlyEmployee {henry_personal_info.name} worked for {henry_contract.hours_worked} and earned {henry.compute_pay()}"
    )
    sarah_personal_info = Person(name="Sarah", id=1)
    sarah_contract = SalariedContract(monthly_salary=10000.)
    sarah_commission = ContractCommission( contracts_landed=10)
    sarah=Employee(personal_info=sarah_personal_info,contract = sarah_contract, commission=sarah_commission)
    
    print(
        f"SalariedEmployee {sarah_personal_info.name} landed {sarah_commission.contracts_landed} and earned {sarah.compute_pay()}"
    )
    bill_personal_info = Person(name="bill", id=10)
    bill_contract = FreeLancerContract(pay_rate=100., hours_worked=100.)
    bill = FreeLancer(personal_info=bill_personal_info, contract=bill_contract)
    print(
        f"Freelancer {bill_personal_info.name} worked for {bill_contract.hours_worked} and earned {bill.compute_pay()}"
    )
    
if __name__ == '__main__':
    main()