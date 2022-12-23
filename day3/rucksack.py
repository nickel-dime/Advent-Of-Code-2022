
def find_value(letter):
    # if letter is uppercase
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def find_common_word(word):
    
    # get the first half of a string
    first_half = word[:len(word) // 2]
    # get the second half of a string
    second_half = word[len(word) // 2:]

    # find common letters between two strings
    common_letters = set(first_half) & set(second_half)
    # convert char to ascii
    ascii_letters = [find_value(letter) for letter in common_letters]
    return ascii_letters[0]

total = 0

with open('day3/input.txt') as f:
    for line in f:
        total += find_common_word(line.strip())

print(total)