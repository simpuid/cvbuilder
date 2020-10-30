FROM python:latest

RUN apt-get update && apt-get install -y texlive-xetex

ADD ./app/requirements.txt /tmp/requirements.txt
RUN pip3 install --no-cache-dir -q -r /tmp/requirements.txt

WORKDIR /app
COPY ./app /app

RUN useradd myuser
RUN chown myuser:myuser -R /app/
USER myuser

CMD gunicorn --bind 0.0.0.0:$PORT  --log-level=debug -t 900 wsgi