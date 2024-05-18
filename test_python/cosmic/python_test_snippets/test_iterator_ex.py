#iterators in contrast to comprehensions and generators

#python for loops dont have indexes 
#what does this mean? 
#means you cant use range for objects which arent sequences like sets
#so python uses iterators for non sequence like objects
#An iterable is an object which returns an iterable and implements 
#__next__() and __iter__()
# 

#collection objects are iterable 
a_set = {1,2,3,4}
for it in a_set:
  print(it)


#
class Obj:
  def __init__(self,name:str,qty:int):
    self.name=name
    self.qty = qty
  def __iter__(self):
        return self
  def __next__(self):
        return 10
      
test_obj = Obj("test",0)
print("test_obj.__iter__:",test_obj.__iter__) 
print(iter(test_obj))

l=[Obj("1",10),Obj("1a",11),Obj("2",20),Obj("3",30)]

#next() triggers StopIteration when done
iterator = iter([1,2,3,4,5])
while 1:
  try:
    print(next(iterator))
  except StopIteration:
    print("stop iteration")
    break



#old
sum_amt=0
for x in l:
  if x.qty<15:
    sum_amt+=x.qty
print("old sum:",sum_amt)

#new
new_sum_amt=(
  x.qty
  for x in l
  if x.qty<15
)
print("new sum:",sum(new_sum_amt))

#this is a lot of boilerplate
#do generators help? 

stuff =  list(x.qty for x in l if x.qty<15)
print(stuff)

one_from_stuff =  next(x.qty for x in l if x.qty<15)
print(one_from_stuff)
#stuff in parenthesis is a generator expression
print(type((x.qty for x in l if x.qty<15)))
