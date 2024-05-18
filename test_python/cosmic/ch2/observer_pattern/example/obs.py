from abc import ABC, abstractmethod
from typing import List
from dataclasses import dataclass,field

@dataclass
class Subscriber:
    name:str
    def notify(self,message):
        print(f"subscriber {self.name}: {message}")

@dataclass
class Observer:
    subs: list = field(default_factory=list)

    def subscribe(self,sub:Subscriber)->None:
        self.subs.append(sub)
    def unsubscribe(self, sub:Subscriber)->None:
        for s in self.subs:
            if s.name==sub.name:
                s.remove(s)
                print("removing sub s:",s)
    def notify_all(self,message:str):
        for s in self.subs:
            s.notify(message)

def test():
    s1 = Subscriber("bob")
    s2 = Subscriber("Sam")
    s3 = Subscriber("ann")
    obs = Observer()
    obs.subscribe(s1)
    obs.subscribe(s2)
    obs.subscribe(s3)
    print(f" observer subs: {obs.subs}")
    obs.notify_all("test_message")
test()
     