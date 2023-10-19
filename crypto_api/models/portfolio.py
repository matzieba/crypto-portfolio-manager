from django.db import models

from crypto_api.models import User


class Coin(models.Model):
    symbol = models.CharField(max_length=256)
    name = models.CharField(max_length=256)


class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    coins = models.ManyToManyField(Coin, through='PortfolioCoin')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Portfolio of {self.user.username}'


class PortfolioCoin(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField()