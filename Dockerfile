FROM python:3.10-slim

WORKDIR /app

COPY app/ /app/app/
COPY whois_scraper.py /app/
COPY cache.py /app/
COPY database.py /app/
COPY test_scraper.py /app/
COPY whois_data.db /app/

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0"]
