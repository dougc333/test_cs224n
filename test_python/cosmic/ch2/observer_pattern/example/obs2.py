from abc import abstractmethod
from dataclasses import field, dataclass
from abc import ABC, abstractmethod

#is this better not sure

class Observer(ABC):
    @abstractmethod
    def notify(message:str):
        pass

@dataclass
class Subscriber(Observer):
    name:str
    def notify(self, msg:str):
        print(f"subscriber {self.name} message:{msg}")

@dataclass
class Subject:
    obs: list = field(default_factory=list)

    def subscribe(self, sub:Subscriber):
        self.obs.append(sub)
    
    def unsubscribe(self, sub:Subscriber):
        for x in obs:
            if x.name == sub.name:
                self.obs.remove(x)
    def notify(self, msg:str):
        for x in self.obs:
            x.notify(msg)

def test():
    s1 = Subscriber("bob")
    s2 = Subscriber("ann")
    s3 = Subscriber("scot")

    s = Subject()
    s.subscribe(s1)
    s.subscribe(s2)
    s.subscribe(s3)
    s.notify("message here")

test()

     
    