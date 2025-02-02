from flask import Flask
from celery import Celery

app=Flask(__name__)
simple_app = Celery('simple_worker', broker='redis://redis:6379/0', backend="redis://redis:6379/0")

@app.route('/simple_start_task')
def call_method():
    app.logger.info("call_method in app.py")
    r = simple_app.send_task('tasks.longtime_add', kwargs={'x':1, 'y':3})
    app.logger.info(r.backend)
    return r.id

@app.route('/simple_task_status/<task_id>')
def get_status(task_id):
    status = simple_app.AsyncResult(task_id, app=simple_app)
    print("get status app.py")
    return "get_status returning" + str(status.state)

@app.route('/simple_task_result/<task_id>')
def task_result(task_id):
    res = simple_app.AsyncResult(task_id).result
    return "task_result in app.py returning:" + str(res)
