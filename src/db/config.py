from sqlalchemy import (MetaData, create_engine)

from databases import Database

from src.core.settings import settings

DATABASE_URL = f'postgresql://{settings.database_user}:{settings.database_password}@{settings.database_host}/{settings.database_name}'

engine = create_engine(DATABASE_URL)
metadata = MetaData()

database = Database(DATABASE_URL)