import json

from matplotlib.font_manager import json_dump

file_path = 'data/habits.py'

def add_habit(data):
    with open(file_path, 'w') as file:
        json_dump(data, file)
        print(data)