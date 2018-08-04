FROM python:3.6-alpine

ARG user_id=1000

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN apk update && apk add dumb-init postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev


RUN adduser -u $user_id stanford -D -H && \
    mkdir /stanford && \
    chown stanford:stanford /stanford

COPY requirements.txt /stanford/requirements.txt
RUN pip install --upgrade pip && pip install -r /stanford/requirements.txt

COPY --chown=stanford:stanford ./stanford/ /stanford/
COPY --chown=stanford:stanford ./run_tests.sh /stanford/
ADD --chown=stanford:stanford docker/entrypoint-*.sh /entry/

RUN mkdir -p /static && chown -R stanford:stanford /static
RUN mkdir -p /media && chown -R stanford:stanford /media

USER stanford
WORKDIR /stanford
ENV PYTHONUNBUFFERED 1

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
