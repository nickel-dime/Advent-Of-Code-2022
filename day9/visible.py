
def parse_input(direction, distance, current_x, current_y):
    if direction == 'U':
        return (current_x, current_y-distance)
    elif direction == 'D':
        return (current_x, distance+current_y)
    elif direction == 'L':
        return (current_x-distance, current_y)
    elif direction == 'R':
        return (distance+current_x, current_y)
            
current_x = 0
current_y = 0  

tail_x = 0
tail_y = 0

visited = set()

def update_tail(tail_x, tail_y, current_x, current_y):
    if abs(tail_x-current_x) >= 2 or abs(tail_y-current_y) >= 2:
        if tail_x == current_x and tail_y == current_y:
            return (tail_x, tail_y)
        # go diagonal
        if tail_y != current_y and tail_x != current_x:
            if abs(tail_x-current_x) == 1:
                tail_x = current_x
                if tail_y > current_y:
                    tail_y -= 1
                else:
                    tail_y += 1
            elif abs(tail_y-current_y) == 1:
                tail_y = current_y
                if tail_x > current_x:
                    tail_x -= 1
                else:
                    tail_x += 1
            else:
                if tail_x > current_x:
                    tail_x -= 1
                else:
                    tail_x += 1
                if tail_y > current_y:
                    tail_y -= 1
                else:
                    tail_y += 1
            return (tail_x, tail_y)

        # go horizontal
        if tail_y == current_y:
            if tail_x > current_x:
                    tail_x -= 1
            else:
                tail_x += 1
            return (tail_x, tail_y)

        # go vertical
        if tail_x == current_x:
            if tail_y > current_y:
                    tail_y -= 1
            else:
                tail_y += 1
            return (tail_x, tail_y)

    return (tail_x, tail_y)

tails = []
# intitialize array of 10 tuples
for i in range(9):
    tails.append((0, 0))

with open('day9/input.txt') as f:
    for line in f:
        direction = line.strip()[0]
        distance = int(line.strip()[2:])

        print(direction, distance)

        for i in range(distance):
            current_x, current_y = parse_input(direction, 1, current_x, current_y)
            tails[0] = update_tail(tails[0][0], tails[0][1], current_x, current_y)
            for i in range(8):
                tails[i+1] = update_tail(tails[i+1][0], tails[i+1][1], tails[i][0], tails[i][1])
            visited.add(tails[-1])
            
            print(tails)

        print('\n\n')

        
print(len(visited))
print(visited)