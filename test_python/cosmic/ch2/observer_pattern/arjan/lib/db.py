
from hashlib import blake2b
from re import U

#why the hell isnt this in a class? make it a class variable? 
users = []

class User:
    def __init__(self,name:str, password:str, email:str):
        self.name = name
        self.password:str=blake2b(password.encode('UTF-8')).hexdigest()
        self.email: str = email
        self.plan:str = "basic"
        self.reset_code:str = ""

    def __repr__(self)-> str:
        return f"Name:{self.name}, EMAIL:{self.email}, PASSWORD:{self.password}"
    
    def reset_password(self, code:str, new_password:str)-> None:
        if code != self.reset_code:
            raise Exception('invalid ')
        self.password = blake2b(new_password.encode('UTF-8')).hexdigest()
    
def create_user(name:str, password:str, email:str)-> User:
    print(f"DB:creating user database entry for {name} and email:{email}")
    new_user = User(name,password,email)
    users.append(new_user)
    return new_user

def find_user(email:str)-> User:
    for u in users:
        if u.email == email:
            return u
    raise Exception("user not found")