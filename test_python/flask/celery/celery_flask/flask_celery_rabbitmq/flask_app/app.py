from flask import Flask
from celery import Celery


app = Flask("__name__")
simple_app = Celery("simple_worker", 
                    broker="amqp://admin:mypass@rabbit:5672", 
                    backend='rpc://')
@app.route("/")
def hi():
  return "hi"

@app.route('/simple_start_task')
def call_method():
    app.logger.info("invoking call_method in app.py")
    r = simple_app.send_task("tasks.longtime_add", kwargs={'x':1,'y':2})
    app.logger.info(r.backend)
    return r.id

@app.route('/simple_task_status/<task_id>')
def get_status(task_id):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    print("invoking method")
    return "status of task:"+str(status.state)
    
@app.route('/simple_task_result/<task_id>')
def task_result(task_id):
    result = simple_app.AsyncResult(task_id).result
    print("task result")
    return "task result "+str(result)
