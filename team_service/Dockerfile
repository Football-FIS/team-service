# syntax=docker/dockerfile:1.4

FROM python:3.10-alpine AS builder
EXPOSE 8000
WORKDIR /team_service
COPY requirements.txt /team_service
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /team_service
ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
