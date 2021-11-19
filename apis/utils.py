import logging
from typing import Any, Dict

import requests
from django.conf import settings

from .serializers import QuoteSerializer

api_base_url = "https://www.alphavantage.co/query"
from_currency = "BTC"
to_currency = "USD"

key = settings.API_KEY_SECRET


def get_exchange_data() -> Dict:
    url = (
        f"{api_base_url}?function=CURRENCY_EXCHANGE_RATE"
        + f"&from_currency={from_currency}&to_currency={to_currency}"
        + f"&apikey={key}"
    )
    try:
        r = requests.get(url)
        data = r.json()
        exchange_data = data.get("Realtime Currency Exchange Rate")
    except Exception as e:
        logging.error(f"raised an error in api request: {e}")
        return {"error": e}
    else:
        logging.info(f"retired exchange_data: {exchange_data}")
        return exchange_data


def save_exchange_data(data: Dict) -> Any:
    try:
        exchange_data = {
            "from_currency": data.get("1. From_Currency Code"),
            "to_currency": data.get("3. To_Currency Code"),
            "exchange_rate": float(data.get("5. Exchange Rate")),
            "last_refreshed": data.get("6. Last Refreshed"),
            "timezone": data.get("7. Time Zone"),
            "bid_price": float(data.get("8. Bid Price")),
            "ask_price": float(data.get("9. Ask Price")),
        }
        serializer = QuoteSerializer(data=exchange_data)
        if serializer.is_valid():
            serializer.save()
            logging.info(f"saved a quote: {serializer.data}")
            return True, serializer.data

        else:
            return False, serializer.errors
    except Exception as e:
        logging.error(f"raised an error in saving exchange_data: {e}")
        return False, {"error": e.__str__}
