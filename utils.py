import requests
import json


class ConvertionExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, ammount: str):
        values = message.text.split(' ')

        if quote == base:
            raise ConvertionExeption(f'Невозомжно перевести одинаковые валюты {base}.')

        try:
            quote_ticker=keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker=keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать валюту {base}')

        try:
            ammount=float(ammount)
        except KeyError:
            raise ConvertionExeption(f'Не удалось обработать количество {ammount}')

            r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
            total_base = json.loads(r.content)[keys[base]]

            return total_base