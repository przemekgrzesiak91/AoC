import itertools as iter

with open('Data/day2.txt') as f:
    input = f.readlines()

part1_result = 0
for row in input:
    row = row.replace('\t',' ').strip().split(' ')
    row = [int(i) for i in row]

    min, max = row[0],row[0]
    for i in row[1:]:
        if min>i: min = i
        elif max<i: max = i
    part1_result += max-min

print(part1_result)


#part 2
https://docs.python.org/3/library/itertools.html
part2_result = 0
for row in input:
    row = row.replace('\t',' ').strip().split(' ')
    row = [int(i) for i in row]

    x = iter.combinations(row,2)
    print(x)

    #for i in row[1:]:



    part2_result += max-min

print(part1_result)


