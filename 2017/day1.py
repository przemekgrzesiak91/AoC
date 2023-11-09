# Day 1 (2017)
from aocd import get_data
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def result(day,year,rp1, rp2):
    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))

day = 1     #Edit this
year = 2017 #Edit this

input = get_data(day = day,year = year)
#print(input)

# Result for part 1
rp1 = 0
# Result for part 2
rp2 = 0

digits = list(str(input))

for i in range(0,len(digits)):
    if i == len(digits)-1:
        if digits[i] ==digits[0]: rp1+=int(digits[i])
    else:
        if digits[i] == digits[i+1]: rp1+=int(digits[i])

dist = int(len(digits)/2)

for i in range(0,len(digits)):
     if i + dist > len(digits)-1:
         break
     else:
         if digits[i] == digits[i+dist]: rp2+=2*(int(digits[i]))

result(day,year,rp1,rp2)