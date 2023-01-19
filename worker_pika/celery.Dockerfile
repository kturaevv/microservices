FROM python:3.11.0-alpine3.16

WORKDIR /usr/src/worker

# adding OpenRC for enabling/starting services
RUN apk update && apk add openrc --no-cache

COPY ./requirements.txt ./
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r ./requirements.txt

# Celery daemon setup
RUN mkdir -p /etc/default

COPY celeryd /etc/init.d/
COPY celeryd.conf /etc/default/celeryd

RUN chmod +x /etc/init.d/celeryd && \
    addgroup celery && \
    adduser celery -G celery -s /bin/sh -D && \
    mkdir -p /var/log/celery/ && chown celery:celery /var/log/celery/ && \
    mkdir -p /var/run/celery/ && chown celery:celery /var/run/celery/ && \
    rc-update add /etc/init.d/celeryd default

COPY . .

CMD ["sh", "./docker-entrypoint.sh"]