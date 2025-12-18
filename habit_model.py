from datetime import datetime, date, timedelta
import json


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
    

        
def show_status():
    with open('data/habits.json', 'r') as f:
        json_obj = json.loads(f.read())
    json_formatted_str = json.dumps(json_obj, indent=2)
    print("The current habits and their status:\n\n")
    print(json_formatted_str)

def complete_habit(args, habits_dict):
    now = datetime.now().strftime(("%Y %m %d"))
    habit_name = args.done[0]
    try:
        habit_entry = habits_dict[f'{habit_name}']
        dates_completed_list = habit_entry['dates_completed']
        if len(dates_completed_list) == 0:
            print("Well done on completing this for the first time!")
            dates_completed_list.append(f'{now}')
        elif dates_completed_list[-1] == now:
            print("You have already completed this habit today!")
        else:
            dates_completed_list.append(f'{now}')
            print("Well done on completing this today!")
    except:
        print("This habit doesn't exist, try creating it first with: -a [habit]")


def add_habit(args, habits_dict):
    habit_name = args.add[0]
    habits_dict = create_habit(habit_name, habits_dict)
    print("Habit added.")
        