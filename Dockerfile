FROM python:3.9-alpine

ADD ./uwsgi.ini /uwsgi/uwsgi.ini
ADD ./requirements.txt /code/requirements.txt

WORKDIR /code/

RUN pip install -U pip
RUN apk add --no-cache \
  ca-certificates gcc musl-dev libffi-dev jpeg-dev zlib-dev postgresql-dev mariadb-dev libressl-dev \
  && pip install uwsgi \
  && pip install -r requirements.txt

ADD . /code

EXPOSE 80

CMD uwsgi --emperor /uwsgi
