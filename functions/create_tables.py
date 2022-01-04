"""Creates tables in the database"""
from utils import engine, Base
import SQL_models.models as models


def table_creator() -> None:
    Base.metadata.create_all(engine)
