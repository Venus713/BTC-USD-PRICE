from config.celery import app

from .utils import get_exchange_data, save_exchange_data


@app.task()
def exchange_data_task():
    exchange_data = get_exchange_data()
    save_exchange_data(exchange_data)
