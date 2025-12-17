import argparse
from datetime import datetime
import json
import os

import habits



def setup_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a','--add',nargs=1, help='This argument allows the user to add a new habit to their tracker.')
    parser.add_argument('-d','--done', nargs=1, help='This argument allows the user to mark the exact time and date that they completed the habit')
    parser.add_argument('-s','--status', action='store_true', help='This argument outputs the list of current habits/streaks')

    args = parser.parse_args()
    return args

def initialise_habits():
    file_path = 'data/habits.json'
    data_template = {
        
    }
    with open(file_path, 'w') as f:
        habits_dict = json.dump(data_template, f)
    return habits_dict

def load_habits():
    file_path = 'data/habits.json'
    habits_dict = {}
    try: 
        file_size = os.path.getsize(file_path)
        if file_size == 0:
            print("File is empty")
            # initialise new habits file
            habits_dict = initialise_habits()
        else:
            print("File is NOT empty")
            # just load in the file
            with open(file_path, 'r') as f:
                habits_dict = json.load(f)
    except FileNotFoundError as e:
        print("File NOT found")
        # initialise new habits file
        habits_dict = initialise_habits()
    return habits_dict

def create_habit(name, dict):
        habit_data = {
        'dates_completed': [],
        }
        dict[f'{name}'] = habit_data
        return dict
    
def save_habits(habits_dict):
    file_path = 'data/habits.json'
    with open(file_path, 'w') as f:
        json.dump(habits_dict, f, indent=4)

if __name__ == '__main__':
    args = setup_args()
    habits_dict = load_habits()
    print(args)
    
    
    if(args.add):
        habit_name = args.add[0]
        habits_dict = create_habit(habit_name, habits_dict)
        print(habits_dict)
    elif(args.done):
        now = datetime.now()
        habit_name = args.done[0]
        habit_entry = habits_dict[f'{habit_name}']
        habits_dict[f'{habit_name}']['dates_completed'].append(f'{now}')

    # elif(args.status):
    #     print('printing status')
    save_habits(habits_dict)