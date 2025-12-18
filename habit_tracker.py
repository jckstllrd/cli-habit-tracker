import argparse
import storage
import habit_model

def setup_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a','--add',nargs=1, help='This argument allows the user to add a new habit to their tracker.')
    parser.add_argument('-d','--done', nargs=1, help='This argument allows the user to mark the exact time and date that they completed the habit')
    parser.add_argument('-s','--status', action='store_true', help='This argument outputs the list of current habits/streaks')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = setup_args()
    
    # Load the JSON file
    habits_dict = storage.load_habits()
    
    # Check which arguments were passed.
    if(args.add):
        habit_model.add_habit(args, habits_dict)
    elif(args.done):
        habit_model.complete_habit(args, habits_dict)
    elif(args.status):
        habit_model.show_status()

    # Save all habits back the JSON file
    habit_model.update_streaks(habits_dict)
    storage.save_habits(habits_dict)