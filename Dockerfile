FROM python:3.13.6

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install --upgrade pip3
RUN pip3 install -r requirements.txt

COPY ./core /app

cmd ["python3","manage.py","runserver","0.0.0.0:8000"]