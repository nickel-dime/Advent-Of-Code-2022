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
    
    def add_left(self, left, wrap=True):
        if self.left:
            raise Exception('already a left')
        
        self.left = left
        if wrap:
            self.left.right = self

    def add_right(self, right, wrap=True):
        if self.right:
            raise Exception('already a right')
        
        self.right = right
        if wrap:
            self.right.left = self

    def add_up(self, up, wrap=True):
        if self.up:
            raise Exception('already a up')
        
        self.up = up
        if wrap:
            self.up.down = self

    def add_down(self, down, wrap=True):
        if self.down:
            raise Exception('already a down')
        
        self.down = down
        if wrap:
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
    line_num = 1
    for line in f:
        line = line.rstrip('\n')
        for i in range(len(line)):
            if line[i] == '.':
                nodes[(line_num, i+1)] = Node(line_num, i+1)

                if not start_node:
                    start_node = nodes[(line_num, i+1)]

        line_num += 1

# if between 0-50 ->
def map_left(old_line_idx):
    match old_line_idx:
        case old_line_idx if 0 < old_line_idx <= 50:
            return (old_line_idx+100, 1)
        case old_line_idx if 50 < old_line_idx <= 100:
            return (101, old_line_idx-50)
        case old_line_idx if 100 < old_line_idx <= 150:
            return (old_line_idx-100, 51)
        case old_line_idx if 150 < old_line_idx <= 200:
            return (1, old_line_idx-100)

def map_right(old_line_idx):
    match old_line_idx:
        case old_line_idx if 0 < old_line_idx <= 50:
            return (old_line_idx+100, 100)
        case old_line_idx if 50 < old_line_idx <= 100:
            return (50, old_line_idx+50)
        case old_line_idx if 100 < old_line_idx <= 150:
            return (old_line_idx-100, 150)
        case old_line_idx if 150 < old_line_idx <= 200:
            return (150, old_line_idx-100)

def map_up(old_line_idx):
    match old_line_idx:
        case old_line_idx if 0 < old_line_idx <= 50:
            return (old_line_idx+50, 51)
        case old_line_idx if 50 < old_line_idx <= 100:
            return (old_line_idx+100, 1)
        case old_line_idx if 100 < old_line_idx <= 150:
            return (200, old_line_idx-100)

def map_down(old_line_idx):
    match old_line_idx:
        case old_line_idx if 0 < old_line_idx <= 50:
            return (1, old_line_idx+100)
        case old_line_idx if 50 < old_line_idx <= 100:
            return (old_line_idx+100, 50)
        case old_line_idx if 100 < old_line_idx <= 150:
            return (old_line_idx-50, 100)

def find_left(lines, line, i, line_idx, node):
    # find the left node it can get to, return None, None if not
    if i-2 >= 0 and line[i-2] == '.':
        if not node.left:
            node.add_left(nodes[(line_idx, i-1)])
    elif i-2>= 0 and line[i-2] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        new_coords = map_left(line_idx)
        if lines[new_coords[0]-1][new_coords[1]-1] == '#':
            return None, None
        else:
            if not node.left:
                node.add_left(nodes[new_coords], wrap=False)


def find_right(lines, line, i, line_idx, node):
    # find the left node it can get to, return None, None if not
    if len(line) > i and line[i] == '.':
        if not node.right:
            return node.add_right(nodes[(line_idx, i+1)])
    elif len(line) > i and line[i] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        new_coords = map_right(line_idx)
        if lines[new_coords[0]-1][new_coords[1]-1] == '#':
            return None, None
        else:
            if not node.right:
                node.add_right(nodes[new_coords], wrap=False)

def find_up(lines, line, i, line_idx, node):
    # find the left node it can get to, return None, None if not
    if line_idx-2 >= 0 and i < len(lines[line_idx-2]) and lines[line_idx-2][i-1] == '.':
        if not node.up:
            return node.add_up(nodes[(line_idx-1, i)])
    elif line_idx-2 >= 0  and i < len(lines[line_idx-2]) and lines[line_idx-2][i-1] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        new_coords = map_up(i)
        if lines[new_coords[0]-1][new_coords[1]-1] == '#':
            return None, None
        else:
            if not node.up:
                node.add_up(nodes[new_coords], wrap=False)

    return None, None

def find_down(lines, line, i, line_idx, node):
    # find the left node it can get to, return None, None if not
    if line_idx < len(lines) and i < len(lines[line_idx]) and lines[line_idx][i-1] == '.':
        if not node.down:
            return node.add_down(nodes[(line_idx+1, i)])
    elif line_idx < len(lines) and i < len(lines[line_idx]) and lines[line_idx][i-1] == '#':
        return None, None
    else:
        # get rightmost value that isn't blank, if . and not the same i return index otherwise return None, None
        # iterate from rightmost to left
        new_coords = map_down(i)
        print(new_coords)
        if lines[new_coords[0]-1][new_coords[1]-1] == '#':
            return None, None
        else:
            if not node.down:
                node.add_down(nodes[new_coords], wrap=False)
            
    return None, None

with open(file_name) as f:
    lines = f.readlines()

    del lines[-1]
    del lines[-1]

    for line_idx, line in enumerate(lines):
        line = line.rstrip('\n')
        for i in range(len(line)):
            if line[i] == '.':
                node = nodes[(line_idx+1, i+1)]

                print(line_idx+1, i+1)

                find_left(lines, line, i+1, line_idx+1, node)
                find_right(lines, line, i+1, line_idx+1, node)

                find_up(lines, line, i+1, line_idx+1, node)
                find_down(lines, line, i+1, line_idx+1, node)

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


print(curr_node.row, curr_node.col, curr_direction)



print(curr_node.row * 1000 + (4 * curr_node.col))