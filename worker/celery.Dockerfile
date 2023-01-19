FROM python:3.11.0-alpine3.16

WORKDIR /usr/src

COPY ./requirements.txt ./
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r ./requirements.txt

COPY . ./worker

CMD celery -A worker.main worker -l INFO