from authm.auth import load_creds 
from datetime import datetime

from gate_api import ApiClient, Order, FuturesApi

from authm.auth import load_creds

def get_api_client():
    client = load_creds("auth/auth.yml")
    api_client = FuturesApi(ApiClient(client))
    return api_client

def get_my_trades():
    settle = 'usdt'
    contract = 'BAT_USDT'
    api_client = get_api_client()
    api_response = api_client.get_my_trades(settle, contract=contract)
    return api_response

