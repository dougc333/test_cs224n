pep526=variable annotations,


this is optional; does not affect runtime
might be part of style guides

some big things

1. classvar

2. variable annotations

id:str #this is a variable annotation

def foo2():
a: List[Any] = []
a.append(1)
a.append("oioouiu")
print(a)

foo2()

# cant write like this anymore

def foo3():
a = []
a.append(1)
a.append("degge")
print(a)

foo3()
