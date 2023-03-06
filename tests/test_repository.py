from datetime import datetime, timezone

import pytest

import psycopg2
from config import config
from contextlib import closing

from persistence.credentials import Credentials_from_file, Credentials_from_input, Encoder_credentials_from_file
from persistence.mapper.memory import MysqlDatabase
from persistence.database_manager import Database_manager

credentials = Credentials_from_file()
database = MysqlDatabase(credentials.params())
db = Database_manager(database=database)


@pytest.mark.asyncio
async def test_add_new_subscriber() -> None:
    data = {'user':'user_test', 'email':'emailtest@example.com'}
    # db._create_user(data)


@pytest.mark.asyncio
async def test_unsubscribe_subscriber() -> None:
    pass


@pytest.mark.asyncio
async def test_unsubscribe_subscriber() -> None:
    pass


@pytest.mark.asyncio
async def test_unsubscribe_subscriber() -> None:
    pass


@pytest.mark.asyncio
async def test_unsubscribe_subscriber() -> None:
    pass


@pytest.mark.asyncio
async def test_unsubscribe_subscriber() -> None:
    pass


    
