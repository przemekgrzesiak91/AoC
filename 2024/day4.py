from colorama import Fore, init
import numpy as np

# Initialize colorama
init(autoreset=True)

day = 4     #Edit this
year = 2024 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'
    with open(filepath, 'r') as f:
        lines = [list(line.strip()) for line in f]

    input = np.array(lines)

    return input

def solve_part1(input):
    """Solve part 1."""

    n,m = np.shape(input)
    result = 0

    for i in range(n):
        for j in range(m):
            current = input[i][j]

            if current =='X':
                words = []
                if i+3<=n:
                    words.append(''.join((input[i:i+4,j])))
                if i-3>=0:
                    words.append(''.join((reversed(input[i-3:i+1, j]))))
                if j+3<=m:
                    words.append(''.join((input[i, j:j+4])))
                if j-3>=0:
                    words.append(''.join(reversed(input[i, j-3:j+1])))
                if i+3<n and j+3<m:
                    words.append(''.join(([input[i+k, j+k] for k in range(4)])))
                if i-3>=0 and j-3>=0:
                    words.append(''.join(([input[i-k, j-k] for k in range(4)])))
                if i+3<n and j-3>=0:
                    words.append(''.join(([input[i+k, j-k] for k in range(4)])))
                if i-3>=0 and j+3<m:
                    words.append(''.join(([input[i-k, j+k] for k in range(4)])))

                result += words.count('XMAS')
    return result

def solve_part2(input):
    """Solve part 2."""

    n, m = np.shape(input)
    result = 0

    for i in range(n):
        for j in range(m):
            current = input[i][j]

            if current == 'A':
                words = []

                if i-1 >=0 and i+1<n and j-1 >=0 and j+1<m:
                     if ''.join([input[i-1+k,j-1+k] for k in range(3)])=="MAS":
                        words.append(1)#down,right

                if i-1 >=0 and i+1<n and j-1 >=0 and j+1 <m:
                      if ''.join([input[i-1+k,j+1-k] for k in range(3)])=="MAS":
                        words.append(2)#down,left

                if i-1 >=0 and i+1 <n and j-1 >=0 and j+1<m:
                      if ''.join([input[i+1-k,j-1+k] for k in range(3)]) =="MAS":
                        words.append(3)#up,right

                if i-1 >=0 and i+1 <n and j-1 >=0 and j+1 <m:
                    if ''.join([input[i+1-k,j+1-k] for k in range(3)]) =="MAS":
                        words.append(4)#up,left

                if 1 in words and 2 in words: result+=1
                if 1 in words and 3 in words: result+=1
                if 2 in words and 4 in words: result+=1
                if 3 in words and 4 in words: result+=1


    return result


def result(day,year):
    input = parse()
    rp1 = solve_part1(input)
    rp2 = solve_part2(input)


    print(Fore.YELLOW + '* ' + Fore.GREEN + 'ADVENT OF CODE ' + str(year)+ Fore.YELLOW + ' *')
    print('Result for ' + Fore.CYAN + 'Day ' + str(day))
    print(Fore.CYAN + str(rp1))
    print(Fore.CYAN + str(rp2))


if __name__ == "__main__":
    result(day,year)
