from authm.auth import load_creds 
from datetime import datetime

from gate_api import ApiClient, Order, SpotApi
##import load_creds func
client = load_creds("auth/auth.yml")
spot_api = SpotApi(ApiClient(client))
#main func
base = "BAT"
quote = "USDT"
trades = spot_api.list_trades(currency_pair=f"{base}_{quote}", limit=2)
print(trades)

