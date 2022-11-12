import pandas as pd
from typing import List, Dict
from db.models import AirQualityParameter
from utils import calculate_aqi_column, calculate_category_column


class Pipeline:
    """
    Gets a list of dictionaries  and loads them into a data frame.
    Contains also the main methods to filter and process the data according to the specifications
    """
    
    def __init__(self, data: List[Dict]):
        self.df: pd.DataFrame = pd.json_normalize(data, sep="_")
        
    def _filter_columns(self):
        columns_to_keep = ['parameter', 'value', 'unit', 'location', 'city', 'country', 'date_utc']
        self.df = self.df.filter(columns_to_keep)
        
    def _filter_rows(self):
        """Filters the rows based on the country, the indices, the averaging period and values"""
        country_filter = self.df['country'].isin(['GB', 'FR', 'NL'])
        parameter_filter = self.df['parameter'].isin(AirQualityParameter.to_list())
        measurement_filter = self.df['averagingPeriod_value'] == 24
        values_filter = self.df['value'] > 0
        self.df= self.df[country_filter & parameter_filter & measurement_filter & values_filter]
        
    def _format_date(self):
        self.df['date_utc'] = pd.to_datetime(self.df['date_utc'])
        
    def _calculate_aqi_value(self):
        self.df['aqi_value'] = self.df.apply(calculate_aqi_column, axis=1)
        
    def _group_by_values(self):
        self.df = self.df.groupby(['parameter', 'city', 'date_utc'], as_index=False).mean(['value', 'aqi_value'])
        
    def _calculate_aqi_category(self):
        self.df['category'] = self.df.apply(calculate_category_column, axis=1)
        
    def filter_by_parameter(self, parameter: AirQualityParameter) -> pd.DataFrame:
        return self.df[self.df['parameter'] == parameter.value]        
        
    def preprocess(self):
        self._filter_rows()
        self._filter_columns()
        self._format_date()
        self._calculate_aqi_value()
        self._group_by_values()
        self._calculate_aqi_category()
        
        

        

