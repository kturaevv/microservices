## Worker microservice

Celery runs as a daemon (background process), while Pika consumes messages from RabbitMQ on a foreground and directs received messages to celery tasks with `delay()` method.

 Celery daemonization is performed by [celeryd](https://docs.celeryq.dev/en/latest/userguide/daemonizing.html#init-script-celeryd)

Run as a standalone service with:
```
# Build and run
make up
# Teardown
make down
```
