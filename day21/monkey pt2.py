monkeys = {}
from sympy import *

with open('day21/input.txt') as f:
    for line in f:
        name = line[:line.index(':')]

        if len(line) < 14:
            number = int(line.strip()[6:])
            monkeys[name] = number
            print(name, number)
        else:
            first_mon = line[6:10]
            operator = line[11]
            second_mon = line.strip()[13:]
            print(first_mon, operator, second_mon)
            monkeys[name] = [first_mon, operator, second_mon]

def solve():
    print(find_name('qwqj'))

op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,}

# monkeys['humn'] = 'x'

def find_name(name):
    if name == 'humn':
        return 'x'

    if type(monkeys[name]) is int:
        return monkeys[name]
    else:
        name1 = find_name(monkeys[name][0])
        name2 = find_name(monkeys[name][2])

        if name1 is not int or name2 is not int:
            return f'({name1}{monkeys[name][1]}{name2})'
        else:
            print(name1, name2)
            return op[monkeys[name][1]](name1, name2)


# solve()

# 52282191702834 = x value 
total = find_name('fflg')

# print(total)

print(sympify('2*(5*x+4) + 3*(2*x-1)'))
print(sympify(total))

# fflg needs to equal 522282191702834

