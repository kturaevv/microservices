from celery import Celery
from kombu import Exchange, Queue

import os, sys

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

IMAGE_QUEUE = os.environ.get("IMAGE_QUEUE")
IMAGE_EXCHANGE = os.environ.get("IMAGE_EXCHANGE")
IMAGE_ROUTING_KEY = os.environ.get("IMAGE_ROUTING_KEY")

celery = Celery(
    'tasks', 
    backend='rpc://', 
    broker=f'pyamqp://{RABBITMQ_HOST}:{RABBITMQ_PORT}',
    task_routes = {
    'tasks.process_img': {'queue': IMAGE_QUEUE, 'exchange':IMAGE_EXCHANGE, 'routing_key':IMAGE_ROUTING_KEY},
}
)

celery.conf.task_queues = (
    Queue(
        IMAGE_QUEUE, 
        Exchange(IMAGE_EXCHANGE, type='topic', durable=False), 
        routing_key=IMAGE_ROUTING_KEY
    ),
)

