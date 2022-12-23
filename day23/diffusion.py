
CUR_LIST = ['N', 'S', 'W', 'E']

elves = {} # mapping of location to elf

class Elf:

    def __init__(self, row, col) -> None:
        self.row = row
        self.col = col

        self.proposed_move = None

    def get_coordinates(self, direction):
        match direction:
            case 'N':
                return [(self.row-1, self.col-1), (self.row-1, self.col), (self.row-1, self.col+1)]
            case 'S':
                return [(self.row+1, self.col-1), (self.row+1, self.col), (self.row+1, self.col+1)]
            case 'W':
                return [(self.row-1, self.col-1), (self.row, self.col-1), (self.row+1, self.col-1)]
            case 'E':
                return [(self.row-1, self.col+1), (self.row, self.col+1), (self.row+1, self.col+1)]

    def check_positions(self, elves):        
        # if no elf is adjacent to this elf return None
        were_elves = False

        for dir in CUR_LIST:
            coords = self.get_coordinates(dir)
            if any(coord in elves for coord in coords):
                were_elves = True
        
        if not were_elves:
            return None

        for dir in CUR_LIST:
            coords = self.get_coordinates(dir)
            if not any(coord in elves for coord in coords):
                self.proposed_move = coords[1]
                return self.proposed_move
        return None

    def move(self, proposed_moves):
        if not self.proposed_move:
            return False
            
        # check if your proposed move is in the list of proposed moves twice
        # if it is not move there and update elves hashmap
        # otherwise do nothing
        if proposed_moves.count(self.proposed_move) == 1:
            elves[self.proposed_move] = elves.pop((self.row, self.col))
            self.row, self.col = self.proposed_move
            self.proposed_move = None
            return True
        return False


with open('day23/input.txt') as f:
    cur_row = 0

    for line in f:
        cur_col = 0
        for char in line.strip():
            if char == '#':
                elves[(cur_row, cur_col)] = Elf(cur_row, cur_col)
            cur_col += 1
        cur_row += 1
    

def round():
    proposed_moves = []
    for elf in elves.values():
        pos = elf.check_positions(elves)
        if pos:
            proposed_moves.append(pos)

    if proposed_moves == []:
        return True

    moves = 0

    copy_elf = elves.copy()
    for elf in copy_elf.values():
        if elf.move(proposed_moves):
            moves += 1
    print(moves)
    
    return False

rounds = 0
for i in range(506):
    rounds += 1
    print('done with round', rounds)
    if round():
        break
    # shift CUR_LIST by 1
    CUR_LIST = CUR_LIST[1:] + CUR_LIST[:1]


min_row = min(elf.row for elf in elves.values())
max_row = max(elf.row for elf in elves.values())
min_col = min(elf.col for elf in elves.values())
max_col = max(elf.col for elf in elves.values())


row_length = max_row - min_row + 1
col_length = max_col - min_col + 1

total_area = (row_length+1) * (col_length+1)

print(total_area - len(elves)) # part 1

# creating image
# area = [['.' for _ in range(max_col - min_col + 1)] for _ in range(max_row - min_row + 1)]
# for elf in elves.values():
#     area[elf.row-min_row][elf.col-min_col] = '#'

# for line in area:
#     print(''.join(line))
