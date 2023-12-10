# Day 7 (2023)
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

day = 7     #Edit this
year = 2023 #Edit this

def parse():
    filepath = 'data/day' + str(day) + '.txt'


    with open(filepath, 'r') as f:
        input = f.readlines()
    return input

def solve_part1(input):
    """Solve part 1."""
    five = []
    four = []
    full = []
    three = []
    two = []
    one = []
    high = []
    rp1 = 0

    ranking = [five, four, full, three, two, one, high]
    new_ranking = []
    
    card_power = {'A':14, 'K':13, 'Q':12, 'J':11, 'T':10,
                  '9':9,  '8':8,  '7':7,  '6':6,  '5':5,
                  '4':4,  '3':3,  '2':2}
    
    for hand in input:
        hand,value= hand.strip().split(' ')
        cards = [hand.count(c) for c in set(hand)]
        hand_translate = [card_power[card] for card in hand]

        if 5 in cards: five.append((hand_translate,value))
        elif 4 in cards: four.append((hand_translate,value))
        elif 3 in cards:
            if 2 in cards: full.append((hand_translate,value))
            else: three.append((hand_translate,value))
        elif cards.count(2) == 2: two.append((hand_translate,value))
        elif cards.count(1) == 5: high.append((hand_translate,value))
        else: one.append((hand_translate,value))

    for group in ranking:
        group = sorted(group, key=lambda cards: cards[0], reverse=True)


        for hand in group:
            new_ranking.append(hand)
    n_hands = len(new_ranking)

    for i in range(0,len(new_ranking)):
        rp1 += int(new_ranking[i][1])*(n_hands-i)
    
    
    return rp1

def solve_part2(input):
    """Solve part 2."""
    five = []
    four = []
    full = []
    three = []
    two = []
    one = []
    high = []
    rp2 = 0

    ranking = [five, four, full, three, two, one, high]
    new_ranking = []

    card_power = {'A': 14, 'K': 13, 'Q': 12, 'J': 1, 'T': 11,
                  '9': 10, '8': 9, '7': 8, '6': 7, '5': 6,
                  '4': 5, '3': 4, '2': 3}

    for hand in input:
        hand, value = hand.strip().split(' ')
        cards = [hand.count(c) for c in set(hand) if c!='J'] or [0]
        hand_translate = [card_power[card] for card in hand]

        countJ = hand.count('J')
        cards.sort(reverse=True)
        cards[0] = cards[0] + countJ

        if 5 in cards:
            five.append((hand_translate, value))
        elif 4 in cards:
            four.append((hand_translate, value))
        elif 3 in cards:
            if 2 in cards:
                full.append((hand_translate, value))
            else:
                three.append((hand_translate, value))
        elif cards.count(2) == 2:
            two.append((hand_translate, value))
        elif cards.count(1) == 5:
            high.append((hand_translate, value))
        else:
            one.append((hand_translate, value))

    for group in ranking:
        group = sorted(group, key=lambda cards: cards[0], reverse=True)

        for hand in group:
            new_ranking.append(hand)

    n_hands = len(new_ranking)

    for i in range(0, len(new_ranking)):
        rp2 += int(new_ranking[i][1]) * (n_hands - i)

    return rp2

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
