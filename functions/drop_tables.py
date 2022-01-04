"""Drops tables from database."""

from utils import engine, Base
import SQL_models.models as models


def table_dropper() -> None:
    """Drops tables from database."""

    Base.metadata.drop_all(engine)
