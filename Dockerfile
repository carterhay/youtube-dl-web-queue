FROM ubuntu:20.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y --no-install-recommends python3 python3-pip ffmpeg
RUN pip3 install youtube-dl flask

ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000
COPY src/ .
CMD ["flask", "run"]
