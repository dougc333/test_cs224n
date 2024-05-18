import numbers
from typing import List,Any


class SomeSequenceObject:
    def __init__(self,list_of_stuff:List[Any]):
        self.data=list_of_stuff
        
    def __len__(self):
        return len(self.data)

    def __getitem__(self,item):
        print("calling getitem")
        return self.data[item]
        

s = SomeSequenceObject([("first",1),(2,"second"),("bob","male")])

def test_len():
    assert len(s)==3
def test_indexing():
    assert s[2] == ("bob","male")
def test_slicing():
    assert list(s[0:1]) == [("first",1)] 
def test_reversed():
    list(reversed(s)) == [('bob', 'male'), (2, 'second'), ('first', 1)]

print("test_len")
test_len()
print("test_indexing")
test_indexing()
print("test_slicing")
test_slicing()
print("test_reversed")
test_reversed()
