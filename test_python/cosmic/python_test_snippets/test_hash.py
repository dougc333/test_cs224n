#POINT: you need __eq__ for objects to get ==
#POINT: you need __hash__ for objects to get set and dict to work
#POINT: you need __gt__ for objects to get sorted to work


#confusing no implementation of __hash__ but object still has hash
#if __eq__ implemented then need __hash__ 
#but can leave both eq and hash off!! Is this a good idea? 
class BadObject:
  def __init__(self,name,id):
    self.name= name
    self.id=id
  #def __eq__(self, other):
  #  return isinstance(other, BadObject) and self.id == other.id    
  #def __hash__(self):
  #  return hash(self.id)
  def __gt__(self,other):
      return self.id > other.id

a = BadObject("a",1)
b = BadObject("b",2)
c = BadObject("c",3)
d = BadObject("a",1)
test_dict={}
test_dict[a] = "one"
test_dict[b] = "two"
test_dict[c] = "three"
print("test_dict:",test_dict)
print(hash(a),hash(b),hash(c))
print("set:",{a,b,c})
print(sorted([a,b,c]))
#if you dont implement __eq__ the problem is you get a==d is false when it hsould be true!!
print("a==b",a==b," a==d",a==d)

#the problem is when you add a list to BadObject then you can have a false equality. 2
#objects are the same but not really because the contents of the list arent compared

class ObjectWithEqualAndHash:
  def __init__(self,name,id):
    self.name= name
    self.id=id
  def __eq__(self, other):
    return isinstance(other, ObjectWithEqualAndHash) and self.id == other.id    
  def __hash__(self):
    print("calling hash")
    return hash(self.id)
  def __gt__(self,other):
      return self.id > other.id

h=ObjectWithEqualAndHash("h",10)
i=ObjectWithEqualAndHash("i",11)
j=ObjectWithEqualAndHash("j",12)
k=ObjectWithEqualAndHash("h",10)
print("h==k",h==k)
#will fail here if no hash, unhashable type
#note we insertd 4 items but 1 is a duplicate so we should only have 3 items for a set. 
#the websearch says hash used for dict keys. This is partially true, also used in set 
print("ObjectWithEqualHadh set:",{h,i,j,k})
print("ObjectWithEqHash List:",[h,i,j,k])
d={}
d[h]="h"
d[i]="i"
d[j]="j"
d[k]="h"

print("ObjectWithEqNoHash dict:",d)
