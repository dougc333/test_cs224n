problem with the runtime error is you dont get a line number where the error occured. 
very difficult to track down

Fundamental problem w/python ABC is you can still instantiate it 
1) add indirection like separate class which tests 
2) add @abstractmethod for __init__

2 design techniques
1) make __init__ an abstract method so subclasses need to implement __init__


When testing for abc.ABC instantion you get a runtime error if you try to instantiate it so it stops the program
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







def test_first_class():
    try:
       fc = FirstClass()
    except:
       print("fc abstract class not instantiated test passed")




need a try except block like this:





def test_instantiate_abc1():
    test_instance = SomeAbstractClass()
    print("is instance:",isinstance(test_instance,abc.ABC))
