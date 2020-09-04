FROM ubuntu:18.04

RUN apt update
RUN apt-get -y install python3 python3-pip speedtest-cli

RUN  mkdir /app
COPY ./requirements.txt /app/requirements.txt
RUN  pip3 install -r /app/requirements.txt
COPY speedtest-exporter.py /app

ENTRYPOINT [ "python3" ]
CMD [ "/app/speedtest-exporter.py" ]
