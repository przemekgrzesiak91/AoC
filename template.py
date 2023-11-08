# Template for Advent of Code.
# Requirement - Advent of code data (https://pypi.org/project/advent-of-code-data/) with your session ID.

from aocd import get_data
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 1     #Edit this
year = 2017 #Edit this

input = get_data(day = day,year = year)
print(input)

# Result for part 1
rp1 = ''
# Result for part 2
rp2 = ''

# Code here

print(rp1)
print(rp2)