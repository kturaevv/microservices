import sys, os, pika, logging

RABBITMQ_HOST=os.environ.get("RABBITMQ_HOST")
Q = os.environ.get("Q_IMAGE_PROCESSING")

# Connect to RabbitMQ
conn = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = conn.channel()
# Create Q if not exists
channel.queue_declare(queue=Q, durable=True)

FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
logging.basicConfig(format=FORMAT, level=logging.INFO)

def main():
    """ Hand written worker task, forever listening to available msgs from Q. """

    def callback(ch, method, properties, body):
        """ Is triggered on every message receive. """
        logging.info("[worker] Received %r" % body)
        # Release task from queue
        channel.basic_ack(delivery_tag = method.delivery_tag)

    # indicate LB policy
    channel.basic_qos(prefetch_count=1)
    # show RabbitMQ that <callback> is responsible for getting msgs
    channel.basic_consume(
        queue=Q,
        on_message_callback=callback
        )
    logging.info(' [*] Waiting for messages. To exit press CTRL+C')
    # Never ending loop for waiting new mesgs
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        logging.info("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)