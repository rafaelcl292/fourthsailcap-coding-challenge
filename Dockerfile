FROM python:latest

ENV TZ=UTC

RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY crontab /etc/cron.d/crontab

COPY scraper.py .
COPY parser.py .
COPY database.py .
COPY create_table.sql .
COPY database.db[t] .

RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab

CMD ["cron", "-f"]

