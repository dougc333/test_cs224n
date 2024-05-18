#python decorator combines 2 features, inner functions and annotations
#the lookup mechanism for annotaions resolves to a fn name. 


def decorator(f):
    def new_function():
        print("decorator here before f")
        f()
        print("decoratoer here after f")
    return new_function


@decorator
def foo():
    print("foo")


foo()

#arguments use kwargs and kw

def decorator_with_args(f):
    def inner_fn(*args, **kwargs ):
        print("before inner arg ")
        f(*args, **kwargs)