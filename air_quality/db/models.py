from sqlalchemy.ext.declarative import declarative_base
from enum import Enum, unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String





@unique
class AirQualityIndex(Enum):
    PM25: str = 'pm25'
    PM10: str = 'pm10'
    O3: str = 'o3'
    NO2: str = 'no2'
    CO: str = 'co'
    
    @classmethod
    def to_list(cls):
        return [index.value  for index in cls.__members__.values()]
    
    

Base = declarative_base()


class DBCountry(Base):
    __tablename__= "country"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    code = Column(String(250), nullable=False)
    