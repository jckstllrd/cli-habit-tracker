import argparse
import json_writer as jw
import json_reader as jr

parser = argparse.ArgumentParser()

parser.add_argument('-a','--add',nargs=1, help='This argument allows the user to add a new habit to their tracker.')
parser.add_argument('-d','--done', nargs=1, help='This argument allows the user to mark the exact time and date that they completed the habit')


args = parser.parse_args()
print(args.add)
print(args.add[0])

data_test = {
    args.add[0]: "today's date"
}

jw.add_habit(data_test)