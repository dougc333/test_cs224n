def foo():
    # never declared not a runtime error
    unknowntype = 10


my_var: int
my_var = 5


class Foo:
    stats = {}


f = Foo()
print(type(f.stats))


class FooWithComment:
    # 'stats' is a class variable
    stats = {}


f1 = FooWithComment()
print(type(f1.stats))

from typing import Any, List


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
