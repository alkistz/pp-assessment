from db.engine import DBSession
from db.models import DBProcessedData
from pydantic import BaseModel
from datetime import datetime


class ProcessedResultsCreateData(BaseModel):
    parameter: str
    city: str
    date_utc: datetime
    value: float
    aqi_value: float
    category: str
   
    
def create_processed_result(data: ProcessedResultsCreateData):
    session = DBSession()
    processed_data = DBProcessedData(**data.dict())
    session.add(processed_data)
    session.commit()