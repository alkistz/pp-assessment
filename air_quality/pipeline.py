import pandas as pd
from typing import List, Dict
from db.models import AirQualityIndex


class Pipeline:
    """
    Gets the filepath to the data files and loads them into a data frame.
    Contains also the main methods to filter and process the data according to the specifications
    """
    
    def __init__(self, data: List[Dict]):
        self.df: pd.DataFrame = pd.json_normalize(data, sep="_")
        
    def filter_according_to_specification(self, countries: List[str], paramaters: List[str]):
        columns_to_keep = ['parameter', 'value', 'unit', 'location', 'city', 'country', 'date_utc']
        country_filter = self.df['country'].isin(countries)
        parameters_filter = self.df['parameter'].isin(paramaters)
        measurement_filter = self.df['averagingPeriod_value'] == 24
        self.filtered_df = self.df[country_filter & parameters_filter & measurement_filter]
        self.filtered_df = self.filtered_df.filter(columns_to_keep)

