
# parse input and get starting pos and ending pos
# create blizzard class with move method that moves and wraps around

# create array of pointers and make first pointer starting pos

# while ending_pos not in pointers, move blizzards and then for each pointer if there is space to go add a pointer
# to pointers list 

starting_pos = None
ending_pos = None

row_height = 0
col_width = 0

class Blizzard:

    def __init__(self, row, col, dir) -> None:
        self.row = row
        self.col = col
        self.dir = dir

    def get_pos(self):
        return (self.row, self.col)

    def move(self):
        if self.dir == '>':
            self.col += 1
        elif self.dir == '<':
            self.col -= 1
        elif self.dir == '^':
            self.row -= 1
        elif self.dir == 'v':
            self.row += 1

        if self.col == 0:
            self.col = col_width - 2
        elif self.col == col_width - 1:
            self.col = 1

        if self.row == 0:
            self.row = row_height - 2
        elif self.row == row_height - 1:
            self.row = 1
    
    def __str__(self) -> str:
        return f'Blizzard: {self.row}, {self.col}, {self.dir}'

class BlizzardManager:
    
    def __init__(self, blizzards, starting_pos, ending_pos) -> None:
        self.blizzards = blizzards
        self.blizzard_positions = None
        self.get_positions()

        self.starting_pos = starting_pos
        self.ending_pos = ending_pos
        self.pointers = [starting_pos]

    def get_positions(self):
        blizzard_positions = set()
        for blizard in self.blizzards:
            blizzard_positions.add(blizard.get_pos())
        
        self.blizzard_positions = blizzard_positions

    def move(self):
        for blizzard in self.blizzards:
            blizzard.move()
        
        self.get_positions()

    def in_bounds(self, coords):
        x = coords[0]
        y = coords[1]
        if (x, y) == self.ending_pos:
            return True

        return x >= 1 and x < row_height-1 and y > 0 and y < col_width-1

    def manhattan(self, first, second):
        # get manhattan distance
        return sum(abs(val1-val2) for val1, val2 in zip(first,second))

    def run(self):
        minutes = 0
        while self.ending_pos not in self.pointers:

            # Used solely for the print statement to see the progress (i.e distance to the end)
            lowest_manhattan_distance, point = None, None
            for pointer in self.pointers:
                manhattan_distance = self.manhattan(pointer, self.ending_pos)
                if lowest_manhattan_distance == None or manhattan_distance < lowest_manhattan_distance:
                    lowest_manhattan_distance = manhattan_distance
                    point = pointer
            # print("Minute", counter, lowest_manhattan_distance, pointer)

            self.move()

            new_pointers = set()
            for pointer in self.pointers:
                # if we can stay still
                if pointer not in self.blizzard_positions and pointer != self.starting_pos:
                    new_pointers.add(pointer)

                # if we can move up
                up = (pointer[0] - 1, pointer[1])
                if self.in_bounds(up) and up not in self.blizzard_positions:
                    new_pointers.add(up)
                
                # if we can move down
                down = (pointer[0] + 1, pointer[1])
                if self.in_bounds(down) and down not in self.blizzard_positions:
                    new_pointers.add(down)
                
                # if we can move left
                left = (pointer[0], pointer[1] - 1)
                if self.in_bounds(left) and left not in self.blizzard_positions:
                    new_pointers.add(left)

                # if we can move right
                right = (pointer[0], pointer[1] + 1)
                if self.in_bounds(right) and right not in self.blizzard_positions:
                    new_pointers.add(right)

            # if there are no expeditions we must restart at the starting position
            if len(new_pointers) == 0:
                new_pointers.add(self.starting_pos)

            self.pointers = new_pointers

            minutes += 1
        
        return minutes


blizzards = []

with open('day24/input.txt') as f:
    lines = f.readlines()
    row_height = len(lines)
    col_width = len(lines[0].strip())
    line_num = 0
    for line in lines:
        if line_num == 0:
            starting_pos = (0, line.index('.'))
        elif line_num == len(lines) - 1:
            ending_pos = (line_num, line.index('.'))
        else:
            char_number = 0
            for char in line.strip():
                if char in ['>', '<', '^', 'v']:
                    blizzards.append(Blizzard(line_num, char_number, char))
                char_number += 1
        line_num += 1
        

# assert(len(blizzards) == 19)
# assert((4, 3) in manager.blizzard_positions)

# part 1
manager = BlizzardManager(blizzards, starting_pos, ending_pos)
first_steps = manager.run()
print(first_steps)

# part 2
new_manager = BlizzardManager(blizzards, ending_pos, starting_pos)
second_steps = new_manager.run()
another_manager = BlizzardManager(blizzards, starting_pos, ending_pos)
third_steps = another_manager.run()
print(first_steps+second_steps+third_steps)
