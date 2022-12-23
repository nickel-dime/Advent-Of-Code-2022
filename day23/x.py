# Input: Lines of "." and "#" characters, implicitly surrounded by more "."
# Output: First half of each round, each # considers its 8 neighbors
#           all blank -> no action
#           N NE NW blank -> plans to go north
#           similar for S W E in that order
#         Second half, each # follows its plan iff only it would move there
#         Round 2, they consider S first; 3, W, etc.
#         What's number of first round where no elf moves?

def get_elf_key(row, column):
    return str(row) + "," + str(column)

def get_row(elf_key):
    parts = elf_key.split(",")
    return int(parts[0])

def get_column(elf_key):
    parts = elf_key.split(",")
    return int(parts[1])

def has_neighbor(row, column, dr, dc):
    elf_key = get_elf_key(row + dr, column + dc)
    if elf_key in coordinates:
        return True
    else:
        return False

def get_new_coordinates(elf_key, planned_direction):
    r = get_row(elf_key)
    c = get_column(elf_key)
    if planned_direction == "N":
        r -= 1
    if planned_direction == "S":
        r += 1
    if planned_direction == "W":
        c -= 1
    if planned_direction == "E":
        c += 1
    return get_elf_key(r, c)

coordinates = {}

input_data = open("day23/input.txt", "r")
row = 0
for input_line in input_data.read().splitlines():
    row += 1
    input_line = input_line.replace("\n", "")
    column = 0
    for character in input_line:
        column += 1
        if character == "#":
            elf_key = get_elf_key(row, column)
            coordinates[elf_key] = True

directions = ["N", "S", "W", "E"]

round = 0
while True:
    round += 1
    number_moves = 0
    planned_directions = {}
    planned_destinations = {}
    elves_with_planned_destination = {}
    for elf_key in coordinates:
        row = get_row(elf_key)
        column = get_column(elf_key)
        has_neighbor_nw = has_neighbor(row, column, -1, -1)
        has_neighbor_n = has_neighbor(row, column, -1, 0)
        has_neighbor_ne = has_neighbor(row, column, -1, 1)
        has_neighbor_w = has_neighbor(row, column, 0, -1)
        has_neighbor_e = has_neighbor(row, column, 0, 1)
        has_neighbor_sw = has_neighbor(row, column, 1, -1)
        has_neighbor_s = has_neighbor(row, column, 1, 0)
        has_neighbor_se = has_neighbor(row, column, 1, 1)
        might_move = {}
        might_move["N"] = (not has_neighbor_nw) and (not has_neighbor_n) and (not has_neighbor_ne)
        might_move["E"] = (not has_neighbor_ne) and (not has_neighbor_e) and (not has_neighbor_se)
        might_move["S"] = (not has_neighbor_se) and (not has_neighbor_s) and (not has_neighbor_sw)
        might_move["W"] = (not has_neighbor_sw) and (not has_neighbor_w) and (not has_neighbor_nw)
        planned_direction = ""
        if might_move["N"] and might_move["E"] and might_move["S"] and might_move["W"]:
            planned_direction = "none"
        else:
            for direction in directions:
                if might_move[direction]:
                    planned_direction = direction
                    break
            if planned_direction == "":
                planned_direction = "none"
        planned_directions[elf_key] = planned_direction
        if planned_direction != "none":
            planned_destination = get_new_coordinates(elf_key, planned_direction)
            planned_destinations[elf_key] = planned_destination
            if not (planned_destination in elves_with_planned_destination):
                elves_with_planned_destination[planned_destination] = []
            elves_with_planned_destination[planned_destination].append(elf_key)
    new_coordinates = {}
    for elf_key in coordinates:
        row = get_row(elf_key)
        column = get_column(elf_key)
        new_location = elf_key
        planned_direction = planned_directions[elf_key]
        if planned_direction != "none":
            planned_destination = planned_destinations[elf_key]
            if len(elves_with_planned_destination[planned_destination]) == 1:
                new_location = planned_destination
                number_moves += 1
        new_coordinates[new_location] = True
    coordinates = new_coordinates
    directions = [
        directions[1],
        directions[2],
        directions[3],
        directions[0]
    ]
    print(round, number_moves)
    if number_moves == 0:
        break

print (round)
