FROM python:3.6.8-alpine3.9

LABEL MAINTAINER="Leonel Aguilar <leoaguilar97@gmail.com>"

ENV GROUP_ID=1000 \
    USER_ID=1000

WORKDIR /var/www/

ADD ./requirements.txt /var/www/requirements.txt
RUN apk add build-base
RUN apk add --no-cache \
        libressl-dev \
        musl-dev \
        libffi-dev \
        freetype-dev \
        libpng-dev \
        jpeg-dev \
        libjpeg-turbo-dev
RUN pip install --upgrade pip
RUN pip install --upgrade Pillow
RUN pip install --upgrade setuptools
RUN pip install Flask-PyMongo
RUN pip3 install --user psutil
RUN pip install -r requirements.txt
ADD . /var/www/
RUN pip install gunicorn

RUN addgroup -g $GROUP_ID www
RUN adduser -D -u $USER_ID -G www www -s /bin/sh

USER www

EXPOSE 5000

CMD [ "gunicorn", "-w", "4", "--bind", "0.0.0.0:5000", "wsgi"]