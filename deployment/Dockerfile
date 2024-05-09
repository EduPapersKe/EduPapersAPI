FROM python:3.12-alpine AS builder

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk update && \
    apk add --no-cache \
    pkgconfig \
    build-base \
    gcc \
    postgresql-dev && \
    rm -rf /var/cache/apk/*

COPY requirements.txt ./  
RUN pip install pip --upgrade -r requirements.txt

FROM python:3.12-alpine

WORKDIR /app

COPY --from=builder /app/ ./  

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
