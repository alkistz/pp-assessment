import os
from db.engine import init_db


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DB_FILE = "sqlite:///" + os.path.join(BASE_DIR, 'air_quality.db')

init_db(DB_FILE)


