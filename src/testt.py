from api import api  # Import the correct function name from the correct module

api = api.get_api_client()  # Call the function to get the trades
trades = api.list_futures_trades()
print(trades)

