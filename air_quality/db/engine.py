from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base


engine: Engine = None
DBSession = sessionmaker()

def init_db(file: str):
    engine = create_engine(file, echo=True)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
    DBSession.bind = engine
    

    