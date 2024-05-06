FROM python:3.12-alpine

RUN apk update && \
    apk add --no-cache \
    pkgconfig \
    build-base \
    gcc \
    postgresql-dev && \
    rm -rf /var/cache/apk/*

WORKDIR /

COPY requirements.txt requirements.txt
COPY manage.py manage.py
COPY root root
COPY api api
COPY users users

RUN pip install --no-cache -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
