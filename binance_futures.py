import logging
import requests
import pprint

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# API
# "https://testnet.binancefuture.com"

# Websocket
# cancel, place, transfer
# "wss://fstream.binance.com"

# Docs
# https://binance-docs.github.io/apidocs/futures

def get_contracts():
    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    print(response_object.status_code)

    contracts = []

    for contract in response_object.json()['symbols']:
        contracts.append(contract['pair'])

    return contracts