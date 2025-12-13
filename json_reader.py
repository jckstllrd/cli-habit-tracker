import json

file_path = "data/habits.json"

with open(file_path, 'r') as f:
    data = json.load()

print(data)