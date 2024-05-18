from guppy import hpy
from memory_profiler import profile
h=hpy()


#unit tests for batch
print(h.heap())
#test_batch_methods()
@profile(precision=4)
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

my_func()


def make_large_file():
    fh = open("large.txt","w")
    for x in range(0,10000000):
        fh.write("this is a text line: "+str(x)+"\n")
    fh.close()
#276M     
make_large_file()
@profile
def read_file():
    with open("large.txt") as fh:
        stuff = fh.readlines()
    print(len(stuff))

read_file()

@profile
def read_file1():
    num_line=0
    with open("large1.txt") as fh:
        single_line = fh.readline()
        num_line+=1
    print("num_line:",num_line)

read_file1()