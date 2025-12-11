import argparse

parser = argparse.ArgumentParser()

parser.add_argument('add', nargs=2, help='This argument allows the user to add a new habit to their tracker.')

args = parser.parse_args()
print(args.add)