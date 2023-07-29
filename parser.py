from html.parser import HTMLParser
from time import strftime


class CurrencyData:
    def __init__(self):
        self.open = None
        self.high = None
        self.low = None
        self.close = None
        self.adj_close = None
        self.filled = False

    def fill(self, data):
        if not self.open:
            self.open = data
        elif not self.high:
            self.high = data
        elif not self.low:
            self.low = data
        elif not self.close:
            self.close = data
        elif not self.adj_close:
            self.adj_close = data
            self.filled = True
        else:
            raise ValueError('CurrencyData is already full')

    def __str__(self):
        return f'Open: {self.open}\n' \
               f'High: {self.high}\n' \
               f'Low: {self.low}\n' \
               f'Close: {self.close}\n' \
               f'Adj Close: {self.adj_close}'


class CurrencyParser(HTMLParser):
    def __init__(self, target=None):
        super().__init__()
        if not target:
            current_month = strftime('%b')
            current_day = strftime('%d')
            current_year = strftime('%Y')
            target = f"{current_month} {current_day}, {current_year}"
        self.target = target
        self.target_found = False
        self.currency_data = CurrencyData()

    def handle_data(self, data):
        if data == self.target:
            self.target_found = True
            return
        if self.target_found and not self.currency_data.filled:
            self.currency_data.fill(data)

