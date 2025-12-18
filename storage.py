import json
import os

file_path = 'data/habits.json'

def initialise_habits():
    data_template = {}
    with open(file_path, 'w') as f:
        habits_dict = json.dump(data_template, f)
    return habits_dict

def load_habits():
    habits_dict = {}
    try: 
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            # print("File is empty")
            # initialise new habits file
            habits_dict = initialise_habits()
        else:
            # print("File is NOT empty")
            # just load in the file
            with open(file_path, 'r') as f:
                habits_dict = json.load(f)
    except FileNotFoundError as e:
        # print("File NOT found")
        # initialise new habits file
        habits_dict = initialise_habits()
    return habits_dict


def save_habits(habits_dict):
    file_path = 'data/habits.json'
    with open(file_path, 'w') as f:
        json.dump(habits_dict, f, indent=4)