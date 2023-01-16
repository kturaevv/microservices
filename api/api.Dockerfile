FROM python:3.11.0-alpine3.16 as builder

WORKDIR /usr/src/app/

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000