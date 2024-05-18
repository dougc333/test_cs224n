#python decorator define your own decorator per function





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