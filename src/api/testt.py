# main.py

import api

api_client = my_api.api()
api_response = api_client.get_my_trades(settle='usdt', contract='BAT_USDT')

print(api_response)

