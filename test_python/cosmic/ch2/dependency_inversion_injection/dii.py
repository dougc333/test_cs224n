from dataclasses import dataclass
import random, string
from abc import ABC, abstractmethod



class Authorizer(ABC):
    @abstractmethod
    def authorize(self):
        pass
    def is_authorized(self)-> bool:
        pass

class Order:
    def __init__(self):
      self.id = ''.join(random.choices(string.ascii_lowercase,k=6))
      self.status="open"
    def set_status(self,status:str):
        self.status = status

class AuthorizerSMS(Authorizer):
    def __init__(self):
        self.authorized = False
        self.code = None

    def generate_sms_code(self):
        self.code=''.join(random.choices(string.digits,k=6))

    def authorize(self):
        code = input("enter sms code")
        self.authorized = code == self.code
        
    def is_authorized(self)-> bool:
        return self.authorized

# class PaymentProcessor:
#     def pay(self,order):
#         authorizer = AuthorizerSMS()
#         authorizer.generate_sms_code()
#         authorizer.authorize()
#         if not authorizer.is_authorized():
#             raise Exception("not authorized")
#         print(f"processing payment for order with {order.id}")
#         order.set_status("paid")
class PaymentProcessor:
    def __init__(self,authorizer:Authorizer):
        self.authorizer = authorizer
    def pay(self,order):
        self.authorizer.authorize()
        if not self.authorizer.is_authorized():
            raise Exception("not auth Payment PRocessor")
        print(f"processingpayment for orderid:{order.id}")
        order.set_status("paid")