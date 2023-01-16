FROM python:3.11.0-alpine3.16

RUN pip3 install --no-cache-dir pika

WORKDIR /usr/src/app

COPY . .

CMD ["python3", "main.py"]