from django.db import models


class Quote(models.Model):
    from_currency = models.CharField(max_length=20, default="BTC")
    to_currency = models.CharField(max_length=20, default="USD")
    exchange_rate = models.FloatField()
    last_refreshed = models.DateTimeField(auto_now_add=True)
    timezone = models.CharField(max_length=50)
    bid_price = models.FloatField()
    ask_price = models.FloatField()

    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "quotes"
