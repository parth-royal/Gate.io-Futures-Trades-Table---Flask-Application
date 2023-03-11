from api import api
from datetime import datetime, timedelta
api = api.get_api_client()
last_trade=None

def get_last_price(contract, return_price_only):
    """
    Args:
    'BAT_USDT'
    """
    global last_trade
    trades = api.list_futures_trades(settle='usdt', contract=contract, limit=1, offset=0)
    assert len(trades) == 1
    trade = trades[0]

    utc_time = datetime.utcfromtimestamp(float(trade.create_time_ms))
    ist_time = utc_time + timedelta(hours=5, minutes=30)

    create_time_formatted = ist_time



    if last_trade and last_trade.id > trade.id:
        logger.debug("STALE TRADEBOOK RESULT FOUND. RE-TRYING.")
        return get_last_price(contract=contract, return_price_only=return_price_only)
    else:
        last_trade = trade

    if return_price_only:
        return trade.price

    logger.info(
        f"LATEST TRADE: {trade.currency_pair} | id={trade.id} | create_time={create_time_formatted} | "
        f"side={trade.side} | amount={trade.amount} | price={trade.price}"
    )
    return trade
x = 'BAT_USDT'

x = get_last_price(x, True)
print(x)

