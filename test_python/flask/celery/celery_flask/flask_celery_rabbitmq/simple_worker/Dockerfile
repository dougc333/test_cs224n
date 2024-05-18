FROM python:3.8

COPY requirements.txt /
RUN pip install -r /requirements.txt

ADD . /simple_worker
WORKDIR /simple_worker
EXPOSE 5672
ENTRYPOINT celery -A tasks worker --loglevel=info
