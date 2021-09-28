FROM python:3.9-alpine

WORKDIR /usr/src/app

# set environment variables
# Prevents from save .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents from bufferin stdout and stderr
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /usr/src/app/requirements.txt


# Installing dependencies to make python work on alpine
RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
    libressl-dev libffi-dev gcc musl-dev python3-dev \
    postgresql-dev bash \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /usr/src/app/requirements.txt \
    && rm -rf /root/.cache/pip


COPY . /usr/src/app/