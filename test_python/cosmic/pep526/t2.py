from typing import Any, ClassVar


# old
class Book:
    ISBN = "Class level ISBN"

    def __init__(self):
        print("init")
        self.isbn: Any = 100
        self.id = 10

    def get_book(self):
        return self.isbn


print(Book.ISBN)
b = Book()
# it inferred init from the default assignment
b.isbn = "instance level ISBN"
b.id = "a new id"
print(b.isbn)
print("dict holds instance variables  b __dict__:", b.__dict__)

# new
class Starship:
    len: int = 10000
    captain: str = "picard"
    num_crew: ClassVar[int] = 1000
    num_captains: int = 1

    def foo(self) -> None:
        print("asdfasfd")


s = Starship()
s.foo()
s.num_captains = 0
Starship.num_captains = 100
s.num_crew = "asdf"
print(Starship.num_crew, s.num_captains, Starship.num_captains, s.num_crew)
print(Starship.__dict__)
