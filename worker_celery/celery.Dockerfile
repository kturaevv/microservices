FROM python:3.11.0-alpine3.16

RUN apk update
RUN pip3 install --upgrade pip

COPY ./requirements.txt ./
RUN pip3 install -r ./requirements.txt

WORKDIR ./usr/src

COPY . ./worker

CMD celery -A worker.worker worker --loglevel=INFO