

class SomeObject:
    def __init__(self,name):
        self.name=name
        
s = SomeObject("asfd")
stuff_dir_fn = dir(s)
stuff_underscore = SomeObject.__dir__(s)
print("stuff_dir_fn:",stuff_dir_fn)
print("\n")
print("stuff_underscore:",stuff_underscore)
stuff_underscore_minus_stuff_dir_fn = list(x for x in stuff_underscore if x not in stuff_dir_fn)
print("\n")
print("stuff_underscore_minus_stuff_dir_fn:",stuff_underscore_minus_stuff_dir_fn)

print("stuff_dir_fn not in stuff_underscore:",list(x for x in stuff_dir_fn if x not in stuff_underscore))