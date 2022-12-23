import re

def check_if_full_overlap(start1, end1, start2, end2):
    return start1 <= start2 and end1 >= end2

total = 0

crates = {}

def parse_crate_location(str):
    index = 0
    for char in line:
        if char == 's':
            index += 1
        else:
            crates.setdefault(index+1, []).append(char)
            index += 1

with open('day5/input.txt') as f:
    for line in f:
        if line.startswith('move'):
            # get all numbers from a string
            numbers = [int(s) for s in re.findall(r'\b\d+\b', line)]
            # print('move ', numbers[0], crates[numbers[1]], ' to ', crates[numbers[2]])
            # pop first three items of list
            move_from = crates[numbers[1]] 
            move_to = crates[numbers[2]]

            stuff_to_move = move_from[:numbers[0]]
            move_from = move_from[numbers[0]:]
            crates[numbers[1]] = move_from
            # reverse stuff_to_move
            stuff_to_move.reverse() # for part 2
            for item in stuff_to_move:
                move_to.insert(0, item)

            print(crates)
            print('\n')

            continue

        line = line.replace('    ', 's').replace('[', '').replace(']', '').replace(' ', '').replace('\n', '')
        if not line.startswith('123'):
            parse_crate_location(line)
        
print(crates)
            
index = 0
word = ''

for i in range(len(crates)):
    word += crates[i+1][0]

print(word)