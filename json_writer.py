import json


file_path = 'data/habits.json'

def add_habit(data):
    with open(file_path, 'w') as file:
        json.dump(data, file)
        print(data)