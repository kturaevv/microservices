import pika, os

RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = os.environ.get('RABBITMQ_PORT')
Q = os.environ.get("Q_IMAGE_PROCESSING")

def send_to_qu(msg: str):
    conn = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = conn.channel()

    # create queue
    channel.queue_declare(queue=Q, durable=True)

    # send msg to queue
    channel.basic_publish(
        exchange='',
        routing_key=Q,
        body=msg,
        properties= pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
        )
    )
    print('[client] sent an image path ...')
    # close conn to ensure successful delivery
    conn.close()

if __name__ == '__main__':
    RABBITMQ_HOST='localhost'
    Q='queue-image-processing'
    msg = input("<msg> to send:")
    send_to_qu(msg if msg is not None else '<default message>')
