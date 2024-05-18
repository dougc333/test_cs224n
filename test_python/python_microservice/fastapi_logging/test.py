import uvicorn
import app_logger
from app_logger_formatter import CustomFormatter

from fastapi import FastAPI,Request,Response
import json
from http import HTTPStatus
import dataclasses
from pydantic.dataclasses import dataclass
from starlette.background import BackgroundTask

app = FastAPI()
@app.middleware("http")
async def log_request(request: Request, call_next):
    response = await call_next(request)
    response.background = BackgroundTask(write_log_data, request, response)
    return response

formatter = CustomFormatter('%(asctime)s')
logger = app_logger.get_logger(__name__, formatter)
status_reasons = {x.value:x.name for x in list(HTTPStatus)}

@dataclass
class User:
    id: int
    name:str
    
user=User(id=1,name="a_name")
user_json = json.dumps(dataclasses.asdict(user))

raw_json={"a":1}
string_json = "{'b':2}"

@app.get('/usrjson')
def hello():
    return user_json

@app.get('/raw_json')
def a():
    return json.dumps(raw_json)

@app.get('string_json')
def b():
    print(string_json)
    return string_json

@app.get("/")
async def root():
    return {"message": "Hello World"}

status_reasons = {x.value:x.name for x in list(HTTPStatus)}

def get_extra_info(request: Request, response: Response):
    return {'req': {
        'url': request.url.path,
        'headers': {'host': request.headers['host'],
                    'user-agent': request.headers['user-agent'],
                    'accept': request.headers['accept']},
        'method': request.method,
        'httpVersion': request.scope['http_version'],
        'originalUrl': request.url.path,
        'query': {}
        },
        'res': {'statusCode': response.status_code, 'body': {'statusCode': response.status_code,
                   'status': status_reasons.get(response.status_code)}}}

def write_log_data(request, response):
    logger.info(request.method + ' ' + request.url.path, extra={'extra_info': get_extra_info(request, response)})


@app.get("/foo")
def foo(request: Request):
    return "success"



if __name__ == '__main__':
    logger.info("Starting server on localhost:8000")
    uvicorn.run(app,host='0.0.0.0',port=8000)

