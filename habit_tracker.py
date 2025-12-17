import argparse
from datetime import datetime, date, timedelta
from hashlib import shake_128
import json
import os
import pandas as pd


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

def create_habit(name, dict):
        habit_data = {
        'dates_completed': [],
        'current_streak': 0,
        }
        dict[f'{name}'] = habit_data
        return dict
    
def update_streaks(habits_dict):
    for habit_name in habits_dict:
        habit = habits_dict[habit_name]
        current_streak = 0
        sliding_date = date.today()
        one_day = timedelta(days=1)
        for date_entry in reversed(habit['dates_completed']):
            
            year, month, day = date_entry.split()
            current_date = date(int(year), int(month), int(day))
            diff = sliding_date - current_date
            # print(f"current date: {current_date}")
            # print(f"sliding date: {sliding_date}")
            # print(f"Result of minusing: {diff}")
            
            if (diff > one_day):
                break
            elif (diff <= one_day):
                
                current_streak += 1
                sliding_date = current_date
                
        habit["current_streak"] = current_streak
    return  
    
def save_habits(habits_dict):
    file_path = 'data/habits.json'
    with open(file_path, 'w') as f:
        json.dump(habits_dict, f, indent=4)


if __name__ == '__main__':
    args = setup_args()
    habits_dict = load_habits()
    
    
    if(args.add):
        habit_name = args.add[0]
        habits_dict = create_habit(habit_name, habits_dict)
        print("Habit added.")
        
    elif(args.done):
        now = datetime.now().strftime(("%Y %m %d"))
        habit_name = args.done[0]
        habit_entry = habits_dict[f'{habit_name}']
        dates_completed_list = habits_dict[f'{habit_name}']['dates_completed']
        added = False
        if len(dates_completed_list) == 0:
            print("Well done on completing this for the first time!")
            dates_completed_list.append(f'{now}')
            added = True
        elif dates_completed_list[-1] == now:
            print("You have already completed this habit today!")
        else:
            dates_completed_list.append(f'{now}')
            print("Well done on completing this today!")
    elif(args.status):

        with open('data/habits.json', 'r') as f:
            json_obj = json.loads(f.read())
        json_formatted_str = json.dumps(json_obj, indent=2)
        print("The current habits and their status:\n\n")
        print(json_formatted_str)
    # Save all habits back the JSON file
    update_streaks(habits_dict)
    save_habits(habits_dict)