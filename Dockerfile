FROM python:3.6-alpine as base

RUN apk update \
    && apk add --no-cache zlib-dev jpeg-dev \
    && rm -rf /var/cache/apk/*

ARG workdir=/usr/src/histograme
WORKDIR $workdir

COPY ./src $workdir

FROM base as builder

COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache build-base \
    && rm -rf /var/cache/apk/* \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt

FROM base as final

LABEL maintainer="sasquatch"

ARG workdir=/usr/src/histograme
WORKDIR $workdir

COPY --from=builder /usr/local /usr/local

ENV LANG C.UTF-8
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
# ENV FLASK_ENV development

EXPOSE 5000

CMD ["flask", "run"]
