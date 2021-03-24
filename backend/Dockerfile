FROM python:3.9-slim

ADD . /usr/src/app/
WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
RUN apt-get autoremove -y gcc

EXPOSE 8000
