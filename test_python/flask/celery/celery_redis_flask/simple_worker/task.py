import time
from celery import Celery
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)

app = Celery('tasks', broker="redis://redis:6379/0", backend="redis://redis:6379/0")

@app.task()
def longtime_add(x,y):
    logger.info("start longtime_add")
    time.sleep(5)
    logger.info("lontime add finished")
    return x+y
