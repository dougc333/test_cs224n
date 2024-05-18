from dataclasses import dataclass,field
from typing import List

@dataclass
class Person:
    first_name:str
    last_name:str
    email_address:str
    friends:List['Person'] = field(default_factory=list, init=False, compare=False, hash=False)
    
    
p1 = Person("bob","x","bobx@example.com")
p2 = Person("bob","x","bobx@example.com")
p2.friends.append(p1)
p3 = Person("bob","z","bobz@example.com")
print("p1:",p1, "p2:",p2)
#default dataclass behavior doesnt compare contents in list.
print(p1==p1,p1==p2)

#
