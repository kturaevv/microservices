FROM python:3.11.0-alpine3.16 as base

WORKDIR /usr/src/app
RUN mkdir data && \
    pip3 install --no-cache-dir requests pika

COPY main.py .