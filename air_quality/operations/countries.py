from db.engine import DBSession
from db.models import DBCountry
from pydantic import BaseModel


class CountryCreateData(BaseModel):
    name: str
    code: str
    

def read_all_countries():
    session = DBSession()
    countries = session.query(DBCountry).all()
    return countries


def create_country(data: CountryCreateData):
    session = DBSession()
    country = DBCountry(**data.dict())
    session.add(country)
    session.commit()