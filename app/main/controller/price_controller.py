from flask import jsonify
import ccxt

from app.main.utils import NotFoundException
import pprint

CURRENCY_TO_BID = 'USDT'

async def get_price(currency):
    
    symbol = f'{currency}/{CURRENCY_TO_BID}'
    exchange = ccxt.kucoin()


    try:
        # Fetch the ticker for the specified currency pair (e.g., 'BTC/USDT')
        ticker = exchange.fetch_ticker(symbol)
        bid_price = ticker['bid']
        
        return {"price": bid_price}
    except ccxt.BadSymbol as e:
        raise NotFoundException(f"Currency pair '{symbol}' not found")

    except ccxt.BaseError as e:
        # Handle exchange errors
        raise e

def get_price_history():
    return jsonify({"price": 100})

def delete_price_history():
    return jsonify({"price": 100})