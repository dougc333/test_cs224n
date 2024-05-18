
class A:
  def __init__(self):
     self.a="Hello"
  def hi(self):
     b="B"
     self.c="C"
  def somefn(self):
     import pdb; pdb.set_trace();
     #is self really defined in this fn? 

a=A()
a.hi()
import pdb;pdb.set_trace()

