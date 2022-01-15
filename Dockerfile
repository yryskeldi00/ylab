FROM python:3.9

ENV PYTHONUNBUFFERED 1
COPY . /app
WORKDIR /app

RUN pip install poetry
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r requirements.txt
