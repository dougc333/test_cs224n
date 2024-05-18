
from dataclasses import dataclass, field
from typing import NamedTuple



@dataclass
class Users:
    name:str

@dataclass
class Publisher:
    publishers: list(NamedTuple)=field(default_factory=list)
    def publish(self, topic:str, me:Users):
        self.publishers.add(NamedTuple(topic, me))



@dataclass
class Subscriber:
    subsribers:list(NamedTuple)=field(default_factory=list)
    def subscribe(self, topic:str, me:  Users):
        self.subscribers.add(NamedTuple(topic, me))
    

