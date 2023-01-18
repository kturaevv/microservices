from celery import Celery
import os

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

def test_celery():
    celery = Celery(
        'tasks', 
        backend='rpc://', 
        broker=f'pyamqp://{RABBITMQ_HOST}:{RABBITMQ_PORT}',
    )
    complexity = 1
    assert celery.send_task("test", (complexity,)).get(timeout=5) == {"Success": complexity}