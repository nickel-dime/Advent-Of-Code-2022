from time import sleep
from random import randint

SIZE = 20
DIFFERENCE = int(500 - (SIZE/2))

grid = []

for i in range(SIZE):
    grid.append(['.'] * SIZE)


grid[0][500-DIFFERENCE] = '.'

for i in range(SIZE):
    grid[11][i] = '#'
    

# 500 -> 100 for 200 so 500-100
# 400 -> 0

# 500 -> 25 for 50 500-25=

highest_y = 0

with open('sample.txt') as f:
    for line in f:
        first = None
        second = None
        third = None
        fourth = None
            
        for val in line.split('->'):
            if first is None:
                first = int(val.split(',')[0].strip())
                second = int(val.split(',')[1].strip())

                if second > highest_y:
                    highest_y = second
            else:
                third = int(val.split(',')[0].strip())
                fourth = int(val.split(',')[1].strip())

                if fourth > highest_y:
                    highest_y = fourth
                # do someething with first, second, third, fourth
                print(first,second, '->', third, fourth)

                if first == third:
                    for i in range(min(second, fourth), max(second, fourth)+1):
                        grid[i][first-DIFFERENCE] = '#'
                elif second == fourth:
                    for i in range(min(first, third), max(first, third)+1):
                        grid[second][i-DIFFERENCE] = '#'
                else:
                    raise Exception('wtf')

                first = third
                second = fourth
                third = None
                fourth = None
            
print(highest_y)
# simulate sand

def add_sand():
    sand_x = 0
    sand_y = 500-DIFFERENCE

    grid[sand_x][sand_y] = 'o'

    while True:
        sand_x, sand_y = find_next_path(sand_x, sand_y)

        if sand_x == -1 and sand_y == -1:
            break
        elif sand_x == -2 and sand_y == -2:
            return False

    return True


def find_next_path(x, y):
    try:
        # straight down
        if grid[x+1][y] == '.':
            grid[x+1][y] = 'o'
            grid[x][y] = '.'
            return (x+1, y)
        # SW
        elif grid[x+1][y-1] == '.':
            grid[x+1][y-1] = 'o'
            grid[x][y] = '.'
            return (x+1, y-1)
        # SE
        elif grid[x+1][y+1] == '.':
            grid[x+1][y+1] = 'o'
            grid[x][y] = '.'
            return (x+1, y+1)

        return (-1, -1)
    except:
        grid[x][y] = '.'
        return (-2,-2)

total = 0
while True:
    if add_sand() and grid[0][500-DIFFERENCE] != 'o':
        total += 1
        sleep(0.1)
        for line in grid:
            print(''.join(line))
    else:
        print(total+1)
        break




# for line in grid:
#     print(''.join(line))

