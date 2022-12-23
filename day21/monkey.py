monkeys = {}

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


def find_name(name):
    if type(monkeys[name]) is int:
        return monkeys[name]
    else:
        print(monkeys[name])
        return op[monkeys[name][1]](find_name(monkeys[name][0]), find_name(monkeys[name][2]))


solve()

# 52282191702834 = x value 