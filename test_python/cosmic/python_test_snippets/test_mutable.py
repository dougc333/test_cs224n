#POINT: objects need hash and eq if you want to equaity comparison and sets. Need .gt. if you want sorted to work

#mutable objects cant be in sets because hash values can change
#all immutable objects ate hashable so they can be in sets
#use default or implement __hash__ to make it look immutabe

#from typing import List

class MutableNoHashEqual:
  def __init__(self,l:list[int]):
    self.a=l
    
    
class Mutable:
  def __init__(self,l:list[int]):
    self.a=l
  def __hash__(self):
      print("hash fn")
      return len(self.a)
  def __eq__(self,other):
      if not isinstance(other,Mutable):
          return False
      return self.a==other.a

a1=MutableNoHashEqual([1,2])
a2=MutableNoHashEqual([3,4])
a3=MutableNoHashEqual([1,2])
print("MutableNoHashEqual a1==a2 should be false:",a1==a2, "MutableNoHashEqual a1==a3 should be true:",a1==a3)

m1=Mutable([1,2])
m2=Mutable([3,4])
m3=Mutable([1,2])
print('should be false, m1==m2:',m1==m2, "m1==m3 should be true:",m1==m3)
print("implementing __hash__ and __equals__ fixes equality comparison.")
print("we didnt test sets since the has implementation isnt correct, we returned a constant and not a correct hash")
m3=Mutable([3,4])
s={m1,m2,m3}
print("2 items in s:",s)
#sets are mutable so you cant put them in sets but you can freeze it
#t={{1,2},{3,4}}
t={frozenset({1,2}),frozenset({3,4})}