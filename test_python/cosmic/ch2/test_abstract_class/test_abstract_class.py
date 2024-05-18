from abc import abstractmethod
import abc
from dataclasses import dataclass
import inspect
#https://docs.python.org/3/library/abc.html
#1) abc.ABC and @abstract method for abstract class usage. 
#2) abstract classes can have impl unlike Java. Can you have data in ABC? 

@dataclass
class SomeAbstractClass(abc.ABC):
    #@abstractmethod
    #def __init__(self):
    #self.name:str="default"
    
    #we are storing data in a class data member which is not widespread practice
    name:str="default"
    @abstractmethod
    def foo():
        raise NotImplementedError
    
class FirstClass(SomeAbstractClass):
    def __init__(self):
        print("FirstClass __init:__")
    
class SecondClass(SomeAbstractClass):
    def __init__(self):
        print("SecondClass __init__ implemented abstract method")
    def foo(self):
        print("SecondClass foo()")



#can you instantiate the abc.ABC?
def test_instantiate_abc():
    try:
      test_instance = SomeAbstractClass()
      print("test_instance:",test_instance)
    except:
      print("test_instantiate_abstract class test passed")
#this doesnt work, you cant use assertions bc of the runtime
#def test_instantiate_abc1():
#    test_instance = SomeAbstractClass()
#    print("is instance:",isinstance(test_instance,abc.ABC))

def test_abstract_abc():
    print("inspect is_abstract:",inspect.isabstract(SomeAbstractClass))
    #cant run this without try/except block
    #print("inspect is_class:",inspect.isclass(SomeAbstractClass()))


def test_first_class():
    try:
       fc = FirstClass("fc ctor")
       print("fc:",fc)
    except:
       print("fc abstract class not instantiated test passed")

def test_second_class():
    try:
       sc = SecondClass()
       assert sc.name == "default" 
       sc.name="asdf"
       assert sc.name == "asdf"
       print("test_second_class test passed")
    except:
       print("test_second_class test failed")

test_instantiate_abc()
test_abstract_abc()
test_first_class()
test_second_class()
   
#how to prevent instantiation of FC. 
#adding try except blocks not best programming style. 
#https://stackoverflow.com/questions/60590442/abstract-dataclass-without-abstract-methods-in-python-prohibit-instantiation