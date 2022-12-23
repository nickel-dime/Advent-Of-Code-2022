import networkx as nx
import matplotlib as plt

G = nx.DiGraph()

# get everything adjacent in 2d array

grid = []

# check if index is valid
def is_valid_index(i, j):
    if i < 0 or j < 0:
        return False
    if i >= len(grid) or j >= len(grid[i]):
        return False
    return True

start = '' 
target = ''

all_ads = []

with open('day12/input.txt') as f:
    line_index = 0
    for line in f:
        new_arr = []
        char_index = 0
        for char in line.strip():
            G.add_node('{},{}'.format(line_index, char_index))

            if char == 'S':
                new_arr.append('a')
                start = '{},{}'.format(line_index, char_index)
                all_ads.append(start)
            elif char == 'E':
                new_arr.append('z')
                target = '{},{}'.format(line_index, char_index)
            else:
                new_arr.append(char)
                if char == 'a':
                    all_ads.append('{},{}'.format(line_index, char_index))

            char_index += 1
        line_index += 1
        grid.append(new_arr)


for line_index in range(len(grid)):
    for char_index in range(len(grid[line_index])):
        curr_ord = ord(grid[line_index][char_index])
        # down
        if is_valid_index(line_index+1, char_index):
            if ord(grid[line_index+1][char_index]) <= curr_ord + 1:
                G.add_edge('{},{}'.format(line_index, char_index), '{},{}'.format(line_index+1, char_index))

        # right
        if is_valid_index(line_index, char_index+1):
            if ord(grid[line_index][char_index+1]) <= curr_ord + 1:
                G.add_edge('{},{}'.format(line_index, char_index), '{},{}'.format(line_index, char_index+1))
        
        # left
        if is_valid_index(line_index, char_index-1):
            if ord(grid[line_index][char_index-1]) <= curr_ord + 1:
                G.add_edge('{},{}'.format(line_index, char_index), '{},{}'.format(line_index, char_index-1))
        
        # up
        if is_valid_index(line_index-1, char_index):
            if ord(grid[line_index-1][char_index]) <= curr_ord + 1:
                G.add_edge('{},{}'.format(line_index, char_index), '{},{}'.format(line_index-1, char_index))


print(start, target)

min_len = 0

for start in all_ads:
    try:
        shortest_path = len(nx.shortest_path(G, source=start, target=target))
        if shortest_path-1 < min_len or min_len == 0:
            min_len = shortest_path-1
    except:
        pass

print(min_len)