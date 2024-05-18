#python has abstract classes and metalasses which can be used to implement abc.ABC
#https://stackoverflow.com/questions/4799401/pythons-super-abstract-base-classes-and-notimplementederror

from abc import ABC,ABCMeta, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak():
        pass
    
#how to enforce the @abstractmethod equivalent using a meta class? 
class SecondAbstract(metaclass = ABCMeta):
    def second():
        pass

class Dog(Animal):
    def __init__(self):
        print("Dog __init__")
    def speak(self):
        print("woof woof")

class S(SecondAbstract):
    def __init__(self):
        print("S __init__")

d = Dog()
s = S()
