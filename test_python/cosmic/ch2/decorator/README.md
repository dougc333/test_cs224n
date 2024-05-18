pytest combines decorators with DI. @pytest.fixture uses decorators and DI. 

Is this true? Is an annotation by definition a decorator? Yes
the problem in decorators come in debugging

a decorator is a nested fn call
decorator(fn) is the same as 

@decorator
def fn()

when you use fn(), it is replaced by decorator(fn())

not a big deal except when you need to debug it .The internal python methods for fn are
no longer there! 


