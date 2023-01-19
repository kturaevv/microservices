from celery import Celery, bootsteps
from kombu import Consumer, Exchange, Queue

import os, sys, logging, requests

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')

IMAGE_QUEUE = os.environ.get("IMAGE_QUEUE")
IMAGE_EXCHANGE = os.environ.get("IMAGE_EXCHANGE")
IMAGE_ROUTING_KEY = os.environ.get("IMAGE_ROUTING_KEY")

FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO, handlers=[logging.StreamHandler(sys.stdout)])

# Declare Kombu Queue
QUEUE = Queue(
        IMAGE_QUEUE, 
        Exchange(IMAGE_EXCHANGE, type='topic', durable=False), 
        routing_key=IMAGE_ROUTING_KEY
    )

class CustomConsumer(bootsteps.ConsumerStep):
    """ A proxy, routes messages directly from Message Queue to celery tasks"""

    def get_consumers(self, channel):
        return [Consumer(channel,
                         queues=[QUEUE],
                         callbacks=[self.handle_message]
                         )]

    def handle_message(self, body, message):
        logging.info(f'[consumer] Received {body}')
        process_img.delay(body)
        message.ack()

app = Celery(
    'worker', 
    backend='rpc://', 
    broker=f'pyamqp://{RABBITMQ_HOST}:{RABBITMQ_PORT}',
)

# Add a proxy class to celery application
app.steps['consumer'].add(CustomConsumer)

# Route messages from specified source to specific task
app.conf.task_routes = {
        'worker.main.process_img': {
            'queue': IMAGE_QUEUE, 
            'exchange':IMAGE_EXCHANGE, 
            'routing_key':IMAGE_ROUTING_KEY
        },
    }

# Declare Queues for celery to listen to
app.conf.task_queues = (
    QUEUE,
)

@app.task
def process_img(image_path):
    logging.info("[task] Received %r" % image_path)
    requests.get("http://app:8000/")
