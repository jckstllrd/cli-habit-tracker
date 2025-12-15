import argparse
import json_writer as jw
import json_reader as jr

parser = argparse.ArgumentParser()

parser.add_argument('-a','--add',nargs=1, help='This argument allows the user to add a new habit to their tracker.')
parser.add_argument('-d','--done', nargs=1, help='This argument allows the user to mark the exact time and date that they completed the habit')
parser.add_argument('-s','--status', action='store_true', help='This argument outputs the list of current habits/streaks')

args = parser.parse_args()
habits = jr.load_habits()

print(habits)

if(args.add):
    print('adding habit')
elif(args.done):
    print('completed habit')
elif(args.status):
    print('printing status')
    


