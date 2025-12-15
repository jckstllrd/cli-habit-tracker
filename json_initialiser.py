import json
from os import write
import habits

def initialise_json():
    file_path = 'data/habits.json'
    habit_dict = habits.create_habits()

    with open(file_path, 'w') as f:
        json.dump(habit_dict, f)