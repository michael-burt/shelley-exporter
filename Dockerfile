FROM python:3.9 AS build-env

COPY . /app
WORKDIR /app

RUN pip3 install -r ./requirements.txt

WORKDIR /app
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages
