import os
from sortedcontainers import SortedList, SortedSet, SortedDict

VALUES = {
    'rock': 1,
    'paper': 2,
    'scissors': 3
}

WIN = {
    'rock': 'paper',
    'paper': 'scissors',
    'scissors': 'rock'
}

LOSE = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}

def convert_from_you_to_string(value, their_move):
    if value == 'X':
        return LOSE[their_move]
    elif value == 'Y':
        return their_move
    elif value == 'Z':
        return WIN[their_move]

def convert_from_opp_to_string(value):
    if value == 'A':
        return 'rock'
    elif value == 'B':
        return 'paper'
    elif value == 'C':
        return 'scissors'

def rock_paper_scissors(your_move, their_move):
    if your_move == 'rock':
        if their_move == 'scissors':
            return 6
        elif their_move == 'paper':
            return 0
        else:
            return 3
    elif your_move == 'paper':
        if their_move == 'rock':
            return 6
        elif their_move == 'scissors':
            return 0
        else:
            return 3
    elif your_move == 'scissors':
        if their_move == 'paper':
            return 6
        elif their_move == 'rock':
            return 0
        else:
            return 3


total_score = 0

with open('day2/input.txt') as f:
    for line in f:
        your_move = None
        their_move = None

        for c in line.strip():
            if c != ' ':
                if their_move is None:
                    their_move = convert_from_opp_to_string(c)
                else:
                    your_move = convert_from_you_to_string(c, their_move)

        if your_move and their_move:
            add_score = rock_paper_scissors(your_move, their_move) + VALUES[your_move]
            total_score += add_score
        else:
            raise Exception("Invalid input")

            
print(total_score)
