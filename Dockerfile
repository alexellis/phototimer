FROM resin/rpi-raspbian:stretch
ENTRYPOINT []

RUN apt-get update -qy \
  && apt-get install -qy python libraspberrypi-bin --no-install-recommends

COPY . .

VOLUME /var/image/

CMD ["python", "take.py", "60"]
