import os

from databases import Database
from sqlalchemy import (
    Column, DateTime, Integer, String,
    Table, MetaData, create_engine)

from sqlalchemy.sql import func


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column('created_at', DateTime, default=func.now(), nullable=False)
)

database = Database(DATABASE_URL)
