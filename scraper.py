from urllib.request import urlopen, Request
from parser import CurrencyParser
from database import insert_data
from datetime import datetime

url = 'https://finance.yahoo.com/quote/BRLUSD%3DX/history'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = {'User-Agent': user_agent}

request = Request(url, headers=headers)
response = urlopen(request)
data = response.read().decode('utf-8')

parser = CurrencyParser()
parser.feed(data)

date = datetime.now().strftime('%Y-%m-%d')
insert_data('BRLUSD', date, parser.currency_data)

