import argparse
from pathlib import Path
import json_writer as jw
import json_reader as jr
import json_initialiser as ji
import habits as hb
import json

parser = argparse.ArgumentParser()

parser.add_argument('-a','--add',nargs=1, help='This argument allows the user to add a new habit to their tracker.')
parser.add_argument('-d','--done', nargs=1, help='This argument allows the user to mark the exact time and date that they completed the habit')
parser.add_argument('-s','--status', action='store_true', help='This argument outputs the list of current habits/streaks')

args = parser.parse_args()

file_path = 'data/habits.json'
habits_file = Path(file_path)
if not habits_file.is_file():
    ji.initialise_json()    
        

habits_dict = jr.load_habits()


if(args.add):
    name = args.add[0]
    habit = hb.new_habit(name)
    habits_dict['habits'].append(habit)

    jw.add_habit(habits_dict)
elif(args.done):
    print('completed habit')
elif(args.status):
    print('printing status')
    


