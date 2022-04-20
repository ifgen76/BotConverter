import json
import requests
from Config import keys, API_KEY


class ConvertionException(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote, base, amount):

        if quote == base:
            raise ConvertionException(f'Невозможно конвертировать одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        pairs = f'{base_ticker}{quote_ticker}'
        r = requests.get(f'https://currate.ru/api/?get=rates&pairs={pairs}&key={API_KEY}')
        total_base = float(json.loads(r.content)['data'][pairs]) * amount
        return (total_base)
