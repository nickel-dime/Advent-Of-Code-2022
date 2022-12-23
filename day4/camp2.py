def check_if_any_overlap(start1, end1, start2, end2):
    return start1 <= start2 <= end1



total = 0

with open('day4/input.txt') as f:
    for line in f:
        # split by comma
        line = line.strip().split(',')
        first_elf = [int(val) for val in line[0].split('-')]
        second_elf = [int(val) for val in line[1].split('-')]

        if check_if_any_overlap(first_elf[0], first_elf[1], second_elf[0], second_elf[1]) or check_if_any_overlap(second_elf[0], second_elf[1], first_elf[0], first_elf[1]):
            total += 1

print(total)