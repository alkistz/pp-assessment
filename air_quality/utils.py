import ndjson
from typing import List, Dict

def load_ndjon(file_path: str) -> List[Dict]:
    with open(file_path) as f:
        return ndjson.load(f)
    
