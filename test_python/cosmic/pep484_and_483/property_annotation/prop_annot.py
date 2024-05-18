#decorators


class TestClass:
    def __init__(self):
        self.name = "some test class"
        self.id = 100
    
    def add_to_id(self, addMe:int):
        self.id += addMe

    
    