import argparse

parser = argparse.ArgumentParser()

parser.add_argument('add', nargs=2, help='This argument allows the user to add a new habit to their tracker.')
parser.add_argument('done', nargs=2, help='This argument allows the user to mark the exact time and date that they completed the habit')


args = parser.parse_args()
print(args)
print(args.add)