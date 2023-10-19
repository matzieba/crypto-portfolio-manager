from django.core.management import BaseCommand

from crypto_api.crypto_api_client.crypto_api_client import CoinGeckoClient


class Command(BaseCommand):
    def handle(self, *args, **options):
        client = CoinGeckoClient()
        geco_coins_list = client.get_coin_list()

