ARG BASE_IMAGE=debian:stretch-slim

FROM $BASE_IMAGE

ARG BASE_IMAGE

LABEL base_image=$BASE_IMAGE

CMD sleep 365d

RUN \
  apt-get update \
  apt-get upgrade -y \
  && apt-get install -y \
    curl \
    ca-certificates \
  && curl -fsS --max-time 120 -o "/usr/bin/hey" https://storage.googleapis.com/hey-release/hey_linux_amd64 \
  && chmod 755 "/usr/bin/hey"


