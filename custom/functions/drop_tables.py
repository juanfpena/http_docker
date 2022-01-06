"""Drops tables from database."""

from custom.SQL_models.utils import engine, Base
import custom.SQL_models.models as models


def table_dropper() -> None:
    """Drops tables from database."""

    Base.metadata.drop_all(engine)
