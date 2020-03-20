FROM python:3-alpine

RUN apk add --update gcc libffi-dev python3-tkinter build-base wget freetype-dev libpng-dev openblas-dev jpeg-dev zlib-dev && \
  apk add musl-dev && \
  # Required by uWSGI
  apk add linux-headers

WORKDIR /

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP run_app.py

EXPOSE 80