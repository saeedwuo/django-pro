FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r requirements.txt


COPY ./core /app