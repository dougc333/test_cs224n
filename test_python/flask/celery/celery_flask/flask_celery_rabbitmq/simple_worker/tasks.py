import time
from celery import Celery
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)
app = Celery('tasks', 
            broker = 'amqp://admin:mypass@rabbit:5672', 
            backend="rpc://")

@app.task()
def longtime_add(x,y):
    logger.info("got request, starting worker")
    time.sleep(4)
    logger.info("task finished")
    return x+y

