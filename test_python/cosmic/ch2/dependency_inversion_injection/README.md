dependency injection refers to not constructing a class in another class

class A:
   def __init__(self):
     b=B()
     b.foo()

class B: 
   def foo(self):
     print(
        "foo"
     )

using dependency injection means b=B() is replaced with an instance. Someone else creates an instance. You dont
care who. 

class A:
   def __init__(self,b):
     b.foo()

We have injected the dependency of class B into A by removing the ctor for class B and adding a reference to an instance


dependency inversion refers to adding an abstract class on top of a concrete class to allow for later expansion. We see this via the strategy pattern 


class A:
   def __init__(self),b:
     b.foo()

class B: 
   def foo(self):
     print("foo")

becomes
from abc import ABC, abstract method


class A:
   def __init__(self,AbstractB.foo),b:
     b.foo()


class AbstractB(ABC):
   def foo(None)->None:
     pass

class B1(AbstractB):
    def foo(None)->None:
     print("foo")
    
class B1(AbstractB):
    def foo(None)->None:
     print("foo B1")
  