from datetime import datetime

import pytest

from app.main.controller.price_controller import (
    delete_price_history, fetch_and_save_currency_price, get_price_history)
from app.main.database import Currency


@pytest.fixture
def clear_currencies_table(test_session):
    test_session.query(Currency).delete()
    test_session.commit()


@pytest.mark.asyncio
async def test_fetch_and_save_currency_price(monkeypatch, test_session, clear_currencies_table):
    async def mock_get_price(currency: str) -> float:
        return 75000.0

    monkeypatch.setattr("app.main.controller.price_controller.get_price", mock_get_price)

    await fetch_and_save_currency_price("BTC", test_session)

    last_record = test_session.query(Currency).order_by(Currency.id.desc()).first()

    assert last_record.currency == "BTC"
    assert last_record.price == 75000.0


@pytest.mark.asyncio
async def test_get_price_history(test_session, clear_currencies_table):
    time_now = datetime.now().replace(microsecond=0)
    test_session.add_all(
        [
            Currency(currency="BTC", date_=time_now, price=60000.0),
            Currency(currency="ETH", date_=time_now, price=2500.0),
            Currency(currency="LTC", date_=time_now, price=150.0),
        ]
    )
    test_session.commit()

    # Fetching price history
    price_history = await get_price_history(test_session)

    assert len(price_history) == 3
    assert price_history[0]["currency"] == "BTC"
    assert price_history[1]["currency"] == "ETH"
    assert price_history[2]["currency"] == "LTC"


@pytest.mark.asyncio
async def test_delete_price_history(test_session, clear_currencies_table):
    time_now = datetime.now().replace(microsecond=0)
    test_session.add_all(
        [
            Currency(currency="BTC", date_=time_now, price=60000.0),
            Currency(currency="ETH", date_=time_now, price=2500.0),
            Currency(currency="LTC", date_=time_now, price=150.0),
        ]
    )
    test_session.commit()
    assert test_session.query(Currency).count() == 3

    # Deleting price history
    response = await delete_price_history(test_session)

    assert response["message"] == "Deleted 3 rows from the PriceHistory table"
    assert test_session.query(Currency).count() == 0
