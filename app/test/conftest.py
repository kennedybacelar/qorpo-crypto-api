import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", "postgresql://username:password@localhost:5433/qorpo_database_test")


@pytest.fixture
def setup_test_database(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", TEST_DATABASE_URL)
    from app.main.database import init_db

    init_db(connect_only=False)


@pytest.fixture(scope="function")
def test_session(setup_test_database):
    Session = sessionmaker(bind=create_engine(TEST_DATABASE_URL))
    with Session() as session:
        yield session
