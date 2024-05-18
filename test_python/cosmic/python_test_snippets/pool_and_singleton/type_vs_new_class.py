

import types

one = type('one', (object,), {'somehash':99})
print(one,type(one))

two = types.new_class('two',(object,), {}, lambda x:x)
print(two,type(two))

#what is the difference between the 2? 
#<class '__main__.one'> <class 'type'>
#<class 'types.two'> <class 'type'>
#looks different, is __main__ part of module namespace? 

#nondefault metaclass
#when do you use this?
class SimleMetaclass(type):
    pass

#when does this not work? 
class Static(object, metaclass=SimleMetaclass):
    pass

another_static_class = types.new_class("a static class",(object,),{"metaclass": SimleMetaclass}, lambda ns: ns)

print("SimleMetaclass:",SimleMetaclass)
print("Static:",Static())
print("another_static_class:",another_static_class)

#the memory allocation and lifecycle for all 3 objects are different!!!

