#a class has to match the functions in protocol.. and you are linked!
from typing import Protocol
from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def talk(self):
        pass
    
class Dog(Animal):
    def talk(self):
        return("woof woof")

class Cat(Animal):
    def talk(self):
        return("meow meow")

def test_abstract():
    print("abstract classes enforce an interface amongst subclasses through the abstract method decorator")
    assert(Dog().talk() == "woof woof")
    assert(Cat().talk() == "meow meow")
    
test_abstract()


class MarineCreature(Protocol):
    def talk(self)-> str:
        pass

class Fish:
    def talk(self)-> str:
        return "bloop bloop"

class Seal:
    def talk(self)-> str:
        return "aarf aarf"

def test_protocol():
    print("protocol types simplify abstract classes by defining a type")
    assert(Fish().talk() == "bloop bloop")
    assert(Seal().talk() == "aarf aarf")

test_protocol()