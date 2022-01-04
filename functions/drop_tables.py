"""Drops tables from database."""

from utils import engine, Base
import models


def table_dropper() -> None:
    """Drops tables from database."""

    Base.metadata.drop_all(engine)
