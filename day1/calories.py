import os
from sortedcontainers import SortedList, SortedSet, SortedDict


print(os.listdir())

maxCalories = 0

currentCalories = 0

ss = SortedList()

with open('day1/calories.txt') as f:
    for line in f:
        if line.strip() == '':
            print(currentCalories)
            ss.add(currentCalories)
            currentCalories = 0
        else:
            currentCalories += int(line.strip())

if currentCalories > maxCalories:
    maxCalories = currentCalories
print(currentCalories)

print('\n', maxCalories)

print(ss)