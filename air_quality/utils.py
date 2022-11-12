import ndjson
from typing import List, Dict
from pandas_profiling import ProfileReport
import pandas as pd
import os
from db.models import AirQualityParameter


# GLOBAL VARIABLES

PM25_CATEGORIES = {
    'good': {
        "low_breakpoint": 0,
        "high_breakpoint": 12.0
    },
    'moderate': {
        "low_breakpoint": 12.1,
        "high_breakpoint": 35.4
    },
    'unhealthy_sensitive': {
        "low_breakpoint": 35.5,
        "high_breakpoint": 55.4
    },
    'unhealthy': {
        "low_breakpoint": 55.5,
        "high_breakpoint": 150.4
    },
    'very_unhealthy': {
        "low_breakpoint": 150.5,
        "high_breakpoint": 250.4
    },
    'hazardous_1': {
        "low_breakpoint": 250.5,
        "high_breakpoint": 350.4
    },
    'hazardous_2': {
        "low_breakpoint": 350.5,
        "high_breakpoint": 500.4
    },
    'hazardous_3': {
        "low_breakpoint": 500.5,
        "high_breakpoint": 99999.9
    }
}


AQI_CATEGORIES = {
    'good': {
        "low_breakpoint": 0,
        "high_breakpoint": 50
    },
    'moderate': {
        "low_breakpoint": 51,
        "high_breakpoint": 100
    },
    'unhealthy_sensitive': {
        "low_breakpoint": 101,
        "high_breakpoint": 150
    },
    'unhealthy': {
        "low_breakpoint": 151,
        "high_breakpoint": 200
    },
    'very_unhealthy': {
        "low_breakpoint": 201,
        "high_breakpoint": 300
    },
    'hazardous_1': {
        "low_breakpoint": 301,
        "high_breakpoint": 400
    },
    'hazardous_2': {
        "low_breakpoint": 401,
        "high_breakpoint": 500
    },
    'hazardous_3': {
        "low_breakpoint": 501,
        "high_breakpoint": 999
    }
}


PM10_CATEGORIES = {
    'good': {
        "low_breakpoint": 0,
        "high_breakpoint": 54
    },
    'moderate': {
        "low_breakpoint": 55,
        "high_breakpoint": 154
    },
    'unhealthy_sensitive': {
        "low_breakpoint": 155,
        "high_breakpoint": 254
    },
    'unhealthy': {
        "low_breakpoint": 255,
        "high_breakpoint": 354
    },
    'very_unhealthy': {
        "low_breakpoint": 355,
        "high_breakpoint": 424
    },
    'hazardous_1': {
        "low_breakpoint": 425,
        "high_breakpoint": 504
    },
    'hazardous_2': {
        "low_breakpoint": 505,
        "high_breakpoint": 604
    },
    'hazardous_3': {
        "low_breakpoint": 604,
        "high_breakpoint": 99999.9
    }
}

PARAMETER_DICT_MAPPING = {
    AirQualityParameter.PM25.value: PM25_CATEGORIES,
    AirQualityParameter.PM10.value: PM10_CATEGORIES
}

# FUNCTIONS

def load_ndjon(file_path: str) -> List[Dict]:
    with open(file_path) as f:
        return ndjson.load(f)
    

def create_data_report(df: pd.DataFrame, title: str):
    profile = ProfileReport(df, title=title)
    profile.to_file(os.path.join("data_reports", "filtered_data",f"{title}.html"))
    
    
def ppm_to_mg_m3(ppm):
    return ppm * 1000



def find_category(value:  int, categories: dict) -> str:
    for category_name, breakpoints in categories.items():
        if value <= breakpoints['high_breakpoint']:
            return category_name
    
    
def calculate_aqi(value, categories):
    category = find_category(value, categories)
    aqi_breakpoints = AQI_CATEGORIES[category]
    parameter_breakpoints = categories[category]
    aqi_1 = (aqi_breakpoints['high_breakpoint'] - aqi_breakpoints['low_breakpoint'])/(parameter_breakpoints['high_breakpoint'] - parameter_breakpoints['low_breakpoint'])
    aqi_2 = (value - parameter_breakpoints['low_breakpoint'])
    return aqi_1 * aqi_2 + aqi_breakpoints['low_breakpoint']


def calculate_aqi_column(row):
    return calculate_aqi(row['value'], PARAMETER_DICT_MAPPING[row['parameter']])


def calculate_category_column(row):
    return find_category(row['value'], PARAMETER_DICT_MAPPING[row['parameter']])
