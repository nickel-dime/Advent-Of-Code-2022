# 1. initialize every node with row/col positions (create node class)

# 2. add connections, include wrapping around

# 3. parse instructions and go through graph

import itertools
import copy

file_name = 'day22/input.txt'

class Node:
    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

        self.left = None
        self.right = None
        self.up = None
        self.down = None
    
    def add_left(self, left):
        if self.left:
            raise Exception('already a left')
        
        self.left = left
        self.left.right = self

    def add_right(self, right):
        if self.right:
            raise Exception('already a right')
        
        self.right = right
        self.right.left = self

    def add_up(self, up):
        if self.up:
            raise Exception('already a up')
        
        self.up = up
        self.up.down = self

    def add_down(self, down):
        if self.down:
            raise Exception('already a down')
        
        self.down = down
        self.down.up = self

    def move(self, direction):
        match direction:
            case 'R':
                return self.right if self.right else self
            case 'L':
                return self.left if self.left else self
            case 'U':
                return self.up if self.up else self
            case 'D':
                return self.down if self.down else self

nodes = {}
start_node = None


with open(file_name) as f:
    line_num = 0
    for line in f:
        line = line.rstrip('\n')
        for i in range(len(line)):
            if line[i] == '.':
                nodes[(i, line_num)] = Node(line_num, i)

                if not start_node:
                    start_node = nodes[(i, line_num)]

        line_num += 1

"""
if left == '.' and not node.left:
    index = i-1 if i-1 >= 0 else len(line)-1
    node.add_left(nodes[(index, line_idx)])

if right == '.' and not node.right:
    index = i+1 if i+1 < len(line) else 0
    node.add_right(nodes[(index, line_idx)])

if up == '.' and not node.up:
    index = line_idx-1 if line_idx-1 >= 0 else len(lines)-1
    node.add_up(nodes[(i, index)])

if down == '.' and not node.down:
    index = line_idx+1 if line_idx+1 < len(lines) else 0
    node.add_down(nodes[(i, index)])
"""

def find_left(line, i):
    # find the left node it can get to, return None, None if not
    if line[i-1] == '.':
        return '.', i-1 if i-1>=0 else len(line)-1
    elif line[i-1] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        for j in range(len(line)-1, -1, -1):
            if line[j] == '#':
                return None, None
            elif line[j] == '.' and j != i:
                return '.', j
            
    return None, None

def find_right(line, i):
    # find the left node it can get to, return None, None if not
    if len(line) > i+1 and line[i+1] == '.':
        return '.', i+1 
    elif len(line) > i+1 and line[i+1] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        for j in range(len(line)):
            if line[j] == '#':
                return None, None
            elif line[j] == '.' and j != i:
                return '.', j
            
    return None, None

def find_up(lines, line, i, line_idx):
    # find the left node it can get to, return None, None if not
    if line_idx-1 >= 0 and i < len(lines[line_idx-1])-1 and lines[line_idx-1][i] == '.':
        return '.', line_idx-1
    elif line_idx-1 >= 0  and i < len(lines[line_idx-1])-1 and lines[line_idx-1][i] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        for j in range(len(lines)-1, -1, -1):
            if i < len(lines[j]) and lines[j][i] == '#':
                return None, None
            elif i < len(lines[j]) and lines[j][i] == '.' and j != line_idx:
                return '.', j
            
    return None, None

def find_down(lines, line, i, line_idx):
    # find the left node it can get to, return None, None if not
    if line_idx+1 < len(lines) and i < len(lines[line_idx+1]) and lines[line_idx+1][i] == '.':
        return '.', line_idx+1
    elif line_idx+1 < len(lines) and i < len(lines[line_idx+1]) and lines[line_idx+1][i] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        for j in range(len(lines)):
            if i < len(lines[j]) and lines[j][i] == '#':
                return None, None
            elif i < len(lines[j]) and lines[j][i] == '.' and j != line_idx:
                return '.', j
            
    return None, None

with open(file_name) as f:
    lines = f.readlines()

    del lines[-1]
    del lines[-1]

    for line_idx, line in enumerate(lines):
        line = line.rstrip('\n')
        for i in range(len(line)):
            if line[i] == '.':
                node = nodes[(i, line_idx)]

                left, left_coord = find_left(line, i)
                right, right_coord = find_right(line, i)

                up, up_coord = find_up(lines, line, i, line_idx)
                down, down_coord = find_down(lines, line, i, line_idx)

                if left == '.' and not node.left:
                    node.add_left(nodes[(left_coord, line_idx)])

                if right == '.' and not node.right:
                    node.add_right(nodes[(right_coord, line_idx)])

                if up == '.' and not node.up:
                    node.add_up(nodes[(i, up_coord)])

                if down == '.' and not node.down:
                    node.add_down(nodes[(i, down_coord)])

def change_direction(cur_dir, new_dir):
    right = {
        'R': 'D',
        'U': 'R',
        'L': 'U',
        'D': 'L'
    }
    left = {
        'R': 'U',
        'U': 'L',
        'L': 'D',
        'D': 'R',
    }

    if new_dir == 'R':
        return right[cur_dir]
    elif new_dir == 'L':
        return left[cur_dir]
    else:
        raise Exception('failed in change_direction', cur_dir, new_dir)


with open(file_name) as f:
    lines = f.readlines()

    input = lines[-1].strip()

    directions = ["".join(x) for _, x in itertools.groupby(input, key=str.isdigit)]

    # bringing it into local scope
    curr_node = start_node
    curr_direction = 'R'

    for distance, direction in zip(directions[0::2], directions[1::2]):
        distance = int(distance)

        print('\n', distance, curr_direction)
        print(curr_node.row, curr_node.col)

        for i in range(distance):
            curr_node = curr_node.move(curr_direction)
            print(curr_node.row+1, curr_node.col+1)


        curr_direction = change_direction(curr_direction, direction)
        print(curr_direction)

            

for i in range(45):
    curr_node = curr_node.move(curr_direction)


print(curr_node.row+1, curr_node.col+1, curr_direction)



