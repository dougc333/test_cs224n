
from typing import Any

class Singleton(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args,**kwargs)
        return cls._instances[cls]

class Logger(metaclass = Singleton):
    def __init__(self):
        print("creating logger")
    def log(self,msg):
        print("logger msg:",msg)

class CustomLogger(Logger):
    def __init__(self):
        print("custom logger")
        super().__init__()

logger = CustomLogger()
logger2 = CustomLogger()
print("loggger:",logger)
print("logger2:",logger2)

logger.log("hello logger")
logger2.log("hello logger2")
