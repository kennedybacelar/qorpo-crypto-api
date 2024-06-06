from datetime import datetime

import ccxt.async_support as ccxt
from sqlalchemy.ext.asyncio import AsyncSession

from app.main.database import Currency
from app.main.model.currency import CurrencyModel
from app.main.utils import NotFoundException

CURRENCY_TO_BID = "USDT"


async def save_data_to_db(currency_model: CurrencyModel, db_session: AsyncSession):

    new_currency = Currency(
        currency=currency_model.currency,
        date_=datetime.now().replace(microsecond=0),
        price=currency_model.price,
    )
    db_session.add(new_currency)
    db_session.commit()

    return new_currency.to_dict()


async def get_price(currency: str) -> float:
    currency_pair_symbol = f"{currency}/{CURRENCY_TO_BID}"
    try:
        exchange = ccxt.kucoin()

        # Fetch the ticker for the specified currency pair (e.g., 'BTC/USDT')
        ticker = await exchange.fetch_ticker(currency_pair_symbol)
        await exchange.close()

        bid_price = ticker["bid"]
        return bid_price

    except ccxt.BadSymbol:
        raise NotFoundException(f"Currency pair '{currency_pair_symbol}' not found")

    finally:
        await exchange.close()


async def fetch_and_save_currency_price(currency: str, db_session: AsyncSession):
    currency_price = await get_price(currency)
    currency_model = CurrencyModel(currency=currency, price=currency_price)
    return await save_data_to_db(currency_model, db_session)


async def get_price_history(db_session: AsyncSession, page: int = 1, page_size: int = 10):

    offset = (page - 1) * page_size

    result = db_session.execute(db_session.query(Currency).offset(offset).limit(page_size))

    rows = result.scalars().all()
    price_history = [row.to_dict() for row in rows]

    return price_history


async def delete_price_history(db_session: AsyncSession):
    count = db_session.query(Currency).delete()
    db_session.commit()
    return {"message": f"Deleted {count} rows from the PriceHistory table"}
