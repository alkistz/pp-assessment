import os
from db.engine import init_db
from utils import load_ndjon
from pipeline import Pipeline
from operations.processed_results import create_processed_result, ProcessedResultsCreateData


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = "sqlite:///" + os.path.join(BASE_DIR, 'air_quality.db')


def main():
    """The main function initiates the DB, runs the pipeline and saves the results in DB"""
    
    
    init_db(DB_FILE)


    data_path = os.path.join('raw_data', 'air_quality')


    data = []
    for filename in os.listdir(data_path):
        data.extend(load_ndjon(os.path.join(data_path, filename)))
        

    air_quality_data = Pipeline(data)
    air_quality_data.preprocess()
    
    for row in air_quality_data.df.to_dict('records'):
        try:
            row_data = ProcessedResultsCreateData(**row)
            create_processed_result(row_data)
        except Exception as e:
            breakpoint()
    

if __name__ == "__main__":
    main()

