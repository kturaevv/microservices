from celery import Celery

import os, sys

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

IMAGE_QUEUE = os.environ.get("IMAGE_QUEUE")
IMAGE_EXCHANGE = os.environ.get("IMAGE_EXCHANGE")
IMAGE_ROUTING_KEY = os.environ.get("IMAGE_ROUTING_KEY")

app = Celery(
    'worker', 
    backend='rpc://', 
    broker=f'pyamqp://{RABBITMQ_HOST}:{RABBITMQ_PORT}',
    include=["worker.celery_tasks"],
    task_cls='worker.celery_tasks:BaseTask'
)

