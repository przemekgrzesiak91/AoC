puzzleInput=[i.strip('\n') for i in open(r'data/day9.txt', 'r').readlines()]
puzzleInput=[i.split(' ') for i in puzzleInput]
puzzleInput=[[int(i) for i in puzzleInput[i]] for i in range(len(puzzleInput))]
def extrapolate(input):
    last=[]
    def returnDifference(list):
        for i in range(len(list)-1):
            input[i]=input[i+1]-input[i]
        last.append(list[len(list)-1])
        list.pop(len(list)-1)
        return list
    while set(input)!={0}:
        input=returnDifference(input)
    return sum(last)
for i in [puzzleInput[106],puzzleInput[167]]:
    print(extrapolate(i))
print('part 1:', sum([extrapolate(i) for i in puzzleInput]))
print('part 2:', sum([extrapolate(i[::-1]) for i in puzzleInput]))