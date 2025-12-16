import json

def load_habits():
    file_path = "data/habits.json"
    with open(file_path, 'r') as f:
        data_dict = json.load(f)
    return data_dict
        
