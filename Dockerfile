FROM alpine:latest

MAINTAINER Andrew Cutler <andrew@panubo.com>

RUN apk update && \
    apk add python py-pip && \
    rm -rf /var/cache/apk/*

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

COPY run.py /run.py

ENTRYPOINT ["/run.py"]
