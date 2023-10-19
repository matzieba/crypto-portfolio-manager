import os

import requests


class APIClient:
    def get_data(self):
        raise NotImplementedError()


class CoinGeckoClient(APIClient):
    def __init__(self):
        self.api_key = os.environ.get("GECKO_COIN_API_KEY", "")
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
        }

    def get_coin_list(self):
        response = requests.get('https://api.coingecko.com/api/v3/coins/list', headers=self.headers)
        return response.json()