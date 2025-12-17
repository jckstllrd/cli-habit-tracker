import argparse
import os



def setup_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-a','--add',nargs=1, help='This argument allows the user to add a new habit to their tracker.')
    parser.add_argument('-d','--done', nargs=1, help='This argument allows the user to mark the exact time and date that they completed the habit')
    parser.add_argument('-s','--status', action='store_true', help='This argument outputs the list of current habits/streaks')

    args = parser.parse_args()
    return args

# def initialise_habits()

def load_habits():
    file_path = 'data/habits.json'
    try: 
        file_size = os.path.getsize(file_path)

        if file_size == 0:
            print("File is empty")
        else:
            print("File is NOT empty")
    except FileNotFoundError as e:
        print("File NOT found")
    return 

if __name__ == '__main__':
    args = setup_args()
    habits_dict = load_habits()
    print(args)
    
    