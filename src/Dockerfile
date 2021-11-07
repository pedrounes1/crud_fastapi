FROM python:3.9-slim as builder

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir ./wheels -r requirements.txt


FROM python:3.9-slim

# RUN addgroup --system app && adduser --system --group app

# USER app

WORKDIR /usr/src/app
COPY --from=builder /usr/src/wheels ./wheels
COPY --from=builder /usr/src/requirements.txt .

RUN pip install --no-cache ./wheels/*

