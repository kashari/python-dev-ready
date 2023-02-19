# https://hub.docker.com/_/python for any other docker image.

FROM python:3.11.2-alpine3.17

WORKDIR /app

COPY app/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY app /app/

CMD ["/bin/bash", "/start-server.sh"]
