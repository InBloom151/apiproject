FROM python:3.9-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY req.txt .

RUN pip install -r req.txt

COPY . .

ENTRYPOINT ["/app/entrypoint.sh"]