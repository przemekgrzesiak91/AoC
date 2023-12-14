import subprocess
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)
'''
Requirement - Advent of code data (pip install advent-of-code-data) with your session ID.
'''

def get_puzzles(year,day_range):
    path0 = str(year) + '/data/day'

    if day_range.isdigit():
        min = int(day_range)
        max = min
    else:
        min,max = [int(x) for x in day_range.split('-')]

    print(min,max)
    for i in range(min, max+1):
        path = path0 + str(i)+'.txt'
        command = ('aocd ' + str(i) + ' ' + year +' > '+ path )

        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()


if __name__ == "__main__":

    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + Fore.YELLOW + ' *')
    year =  input("Get your puzzles based on your session ID \nYear of AOC: ")
    day_range = input("Enter day or days, for which you need puzzles (eg. 1 - mean day1, 1-5 means days 1-5)\nDay(s):")

    get_puzzles(year, day_range)