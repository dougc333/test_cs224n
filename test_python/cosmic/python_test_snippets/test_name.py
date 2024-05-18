

class foo:
    def __init__(self):
        self.a=10
        self._b=20
        self.__c=30
f=foo()
print(f.__dict__)
print(f,f.a,f._b,f.__c)

