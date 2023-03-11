from authm.auth import load_creds 
from datetime import datetime

from gate_api import ApiClient, Order, FuturesApi
##import load_creds func
client = load_creds("auth/auth.yml")
api = FuturesApi(ApiClient(client))
#main func
base = "BAT"
quote = "USDT"
#trades = spot_api.list_trades(currency_pair=f"{base}_{quote}", limit=2)
#print(trades)


currency_pair = 'BAT_USDT'
#api_response = spot_api.get_fee(currency_pair=currency_pair)
#print(api_response)


settle = 'usdt' 

contract = 'BAT_USDT'

api_response = api.get_my_trades(settle, contract=contract)
print(api_response)
