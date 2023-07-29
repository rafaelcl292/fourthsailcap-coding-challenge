import unittest
from parser import CurrencyParser


class TestCurrencyParser(unittest.TestCase):
    def setUp(self):
        self.parser = CurrencyParser('Jul 14, 2023')
        with open('tests_inputs/EURUSD_14-7.html', 'r') as f:
            self.parser.feed(f.read())

    def test_open(self):
        self.assertEqual(self.parser.currency_data.open, '1.1223')

    def test_high(self):
        self.assertEqual(self.parser.currency_data.high, '1.1245')

    def test_low(self):
        self.assertEqual(self.parser.currency_data.low, '1.1206')

    def test_close(self):
        self.assertEqual(self.parser.currency_data.close, '1.1223')

    def test_adj_close(self):
        self.assertEqual(self.parser.currency_data.adj_close, '1.1223')

    def test_data_not_found(self):
        parser = CurrencyParser('Jul 32, 2023')
        with open('tests_inputs/EURUSD_14-7.html', 'r') as f:
            parser.feed(f.read())
        self.assertIsNone(parser.currency_data.open)
        self.assertIsNone(parser.currency_data.high)
        self.assertIsNone(parser.currency_data.low)
        self.assertIsNone(parser.currency_data.close)
        self.assertIsNone(parser.currency_data.adj_close)


if __name__ == '__main__':
    unittest.main()

