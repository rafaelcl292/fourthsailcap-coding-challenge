from urllib.request import urlopen, Request
from parser import CurrencyParser
from database import insert_data
from datetime import datetime

currency_pairs = [
    'BRLUSD',
    'EURUSD',
    'CHFUSD',
    'EURCHF',
]

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
headers = {'User-Agent': user_agent}
date = datetime.now().strftime('%Y-%m-%d')

for currency_pair in currency_pairs:
    url = f'https://finance.yahoo.com/quote/{currency_pair}%3DX/history'
    request = Request(url, headers=headers)
    response = urlopen(request)
    data = response.read().decode('utf-8')

    parser = CurrencyParser()
    parser.feed(data)

    insert_data(currency_pair, date, parser.currency_data)

