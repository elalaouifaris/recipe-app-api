FROM python:3.9-alpine

ENV PYTHONUNBEFFERED 1

RUN apk update && apk add python3-dev \
                          gcc \
                          libc-dev

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user