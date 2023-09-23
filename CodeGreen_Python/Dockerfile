FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y python3-pip

COPY ./app /app
WORKDIR /app
RUN set -ex && \
    pip3 install -r requirements.txt

CMD ["python3", "app.py"]