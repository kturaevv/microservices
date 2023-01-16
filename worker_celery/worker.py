from celery import Celery

import os, sys

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')
Q_IMAGE_PROCESSING = os.environ.get("Q_IMAGE_PROCESSING")

celery = Celery(
    'tasks', 
    backend='rpc://', 
    broker=f'pyamqp://{RABBITMQ_HOST}:{RABBITMQ_PORT}',
    task_cls='worker.tasks:BaseTask',
    task_routes = {
        'tasks.process_img': {'queue': Q_IMAGE_PROCESSING},
    },
)
