FROM python:3.8.0a3-alpine
WORKDIR /app
COPY . /app
RUN apk add libreoffice