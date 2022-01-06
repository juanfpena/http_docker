"""Creates tables in the database"""

import custom.SQL_models.models as models
from custom.SQL_models.utils import engine
from custom.SQL_models.models import Base




def table_creator() -> None:
    Base.metadata.create_all(engine)
