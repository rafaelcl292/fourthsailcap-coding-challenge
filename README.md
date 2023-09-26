# scraper-coding-challenge

Python application that scrapes daily currency prices from Yahoo Finance and stores it into a SQLite database.

The scraper exclusively employs Python's built-in modules.

## Docker
Start the aplication with docker
```
docker build -t scraper .
```
```
docker run -d --rm --name scraper-container scraper
```
Save the database from the docker container with
```
docker cp scraper-container:app/database.db .
```
Stop the aplication
```
docker container stop scraper-container
```
To change the frequency and schedule of scraper modify [`crontab`](https://github.com/rafaelcl292/fourthsailcap-coding-challenge/blob/main/crontab) (UTC)

## Without Docker
To run the scraper without docker simply run (won't activate a cronjob)
```
python scraper.py
```

## Testing
To run tests
```
python tests.py
```
