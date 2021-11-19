from rest_framework import serializers

from .models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
            "from_currency",
            "to_currency",
            "exchange_rate",
            "last_refreshed",
            "timezone",
            "bid_price",
            "ask_price",
        )

    def __init__(self, *args, **kwargs):
        super(QuoteSerializer, self).__init__(*args, **kwargs)
