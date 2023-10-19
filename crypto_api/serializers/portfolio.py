from rest_framework import serializers

from crypto_api.models import Coin, PortfolioCoin, Portfolio


class CoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coin
        fields = ('id', 'symbol', 'name')


class PortfolioCoinSerializer(serializers.ModelSerializer):
    coin = CoinSerializer(read_only=True)

    class Meta:
        model = PortfolioCoin
        fields = ('id', 'coin', 'quantity', 'purchase_price', 'purchase_date')


class PortfolioSerializer(serializers.ModelSerializer):
    coins = PortfolioCoinSerializer(source='portfoliocoin_set', many=True, read_only=True)

    class Meta:
        model = Portfolio
        fields = ('id', 'user', 'coins')
