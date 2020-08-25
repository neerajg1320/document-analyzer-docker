FROM python:3.7-alpine as base
FROM quoinedev/python3.7-pandas-alpine as pandas-base

FROM pandas-base as builder

# set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apk update
#RUN apk add poppler-utils
#RUN apk add postgresql-dev gcc python3-dev musl-dev

##
RUN apk update
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev \
        zlib zlib-dev

# For python pdftotext library
RUN apk add --update g++
RUN apk add --update poppler-dev

# Needed if we want command pdftotext to be available
RUN apk add --update poppler-utils
##


RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt ./
RUN pip install --install-option="--prefix=/install" -r requirements.txt

RUN apk del .tmp-build-deps


## Second Phase
FROM pandas-base
ENV PYTHONUNBUFFERED 1

COPY --from=builder /install /usr/local

RUN mkdir /app
WORKDIR /app

RUN mkdir /database
COPY /api-server/postgres_database_dump.sql /database

COPY api-server/app /app

RUN apk add postgresql-dev
RUN apk add poppler-utils
RUN apk add postgresql-client

CMD ["/bin/sh"]