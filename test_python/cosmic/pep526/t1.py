from typing import List, get_type_hints

from typing_extensions import reveal_type

# OLD
a = 10
# new
b: int = 20

# old
# primes is a list of integers
primes = []  # type: List[int]
print("std type:", type(primes))
print("reveal type:", reveal_type(primes))

primes.append(3)
primes.append("aaaa")
print(primes)
from typing import Any

# new
p: List[Any] = []
p.append(3)
p.append(0.143)
p.append("hi")
print(p)
# not worth time...thisis cmpletely optional, runtime
# ignores all the type hints. only for static checking for tools
#
import __main__

print("__main__ type hints:", get_type_hints(__main__))
print("global __annotations__:", __annotations__)
