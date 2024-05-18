
# from functools import reduce
from typing import Callable
from typing import Union
# Callable[[Arg1Type, Arg2Type], ReturnType] Callable is rejected!
# move to 2 ints then subclass and add 2 int fns


def twotypes(a: int) -> Union[int, str, None]:
    if a % 2 == 1:
        return "odd"
    elif a % 2 == 0:
        return 0


class Sum:
    def __init__(self, a: int | float, b: int | float):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a+self.b


def some_fn(a: int) -> None:
    print(f"some fn {a}")
# https://medium.com/python-pandemonium/function-as-objects-in-python-d5215e6d1b0d


def printEven(a: list[int]) -> None:
    [print(x) for x in a if x % 2 == 0]


def returnStr() -> str:
    return "hi"


def return_fn() -> Callable[..., str]:
    return returnStr


def return_fn2(fn: Callable[..., None]) -> Callable[..., str]:
    return returnStr


if __name__ == '__main__':
    l = [1, 2, 3, 4]
    [some_fn(x) for x in l]
    print("end 1")
    printEven([1, 3, 4])
    print("end2")
    print(returnStr())
    print("end3")

    # return_fn2(foo)
