
def find_value(letter):
    # if letter is uppercase
    if letter.isupper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96

def find_common_word(word1, word2, word3):
    # find common letters between two strings
    common_letters = set(word1) & set(word2) & set(word3)
    # convert char to ascii
    ascii_letters = [find_value(letter) for letter in common_letters]
    print(common_letters, ascii_letters)
    return ascii_letters[0]

total = 0

with open('day3/input.txt') as f:
    # loop through every 3 lines in the file
    for line1, line2, line3 in zip(f, f, f):
        total += find_common_word(line1.strip(), line2.strip(), line3.strip())

print(total)