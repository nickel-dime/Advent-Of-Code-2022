
def check_number_greater_than(value, list1):
    total = 0
    for x in list1:
        if value > x:
            total += 1
        elif value == x:
            total += 1
            break
        else:
            total += 1
            break

    if total == 0:
        return 1

    return total


def is_visible(value, left, right, top, down):
    # reverse a list 
    left.reverse()
    top.reverse()

    left = check_number_greater_than(value, left) 
    right = check_number_greater_than(value, right) 
    top = check_number_greater_than(value, top) 
    down = check_number_greater_than(value, down)

    total = left * right * top * down
    return total

grid = []

with open('day8/input.txt') as f:
    for line in f:
        current_line = []
        for x in line.strip():
            current_line.append(int(x)) 

        grid.append(current_line)

total_visible = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        curr_value = grid[i][j]

        left = grid[i][:j]
        top = []
        for x in grid[:i]:
            top.append(x[j])
            
        print('\n')

        if j == len(grid[i]) - 1:
            down = []
        else:
            down = []
            for x in grid[1+i:]:
                down.append(x[j])
        
        if i == len(grid) - 1:
            right = []
        else:
            right = grid[i][j+1:]
        
        new_num = is_visible(curr_value, left, right, top, down)
        print(new_num, i, j)

        if new_num > total_visible:
            total_visible = new_num

print(total_visible)