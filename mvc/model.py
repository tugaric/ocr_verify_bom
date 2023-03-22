import json

class My_model:
    def __init__(self):
        self.data = []

def from_json_file(filename):
    dicts = []
    with open(filename, 'r') as f:
        data = json.load(f)
        for item in data:
            if isinstance(item, dict):
                dicts.append(item)
    return dicts