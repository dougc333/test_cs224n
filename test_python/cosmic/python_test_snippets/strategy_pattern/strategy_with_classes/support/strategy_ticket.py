
from dataclasses import dataclass, field
import random


@dataclass
class SupportTicket:
    customer:str
    issue:str
    id:str = field(init=False)
    
    def __post_init__(self):
        self.id =  self.generate_id()
    
    def process(self):
        print("--------------------")
        print(f"processing ticket id:{self.id}")
        print(f"customer:{self.customer}")
        print(f"Issue:{self.issue}")      
        print("--------------------")
    def generate_id(self):
        return str(random.randint(0,100))
        