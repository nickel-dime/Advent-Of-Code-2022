
class Item:

    def __init__(self, worry_level):
        self.worry_level = worry_level

    def inspect_item(self, operation):
        self.worry_level = operation(self.worry_level)

        # divide worry level by 3 and round down to nearest int
        # self.worry_level = self.worry_level // 3

        # make it divisor of 9,699,690
        self.worry_level = self.worry_level % 9699690


class Monkey:
    
    def __init__(self, name, items : list[Item], operation, test, true, false):
        """
        :param items: list of items to iterate over
        :param operation: operation to perform on each item : lambda (num) -> num
        :param test: test to perform on each item : lambda (num) -> bool
        :param true: monkey to thow to if test is true : Monkey
        :param false: monkey to throw to if test is false : Monkey
        """
        self.name = name
        self.items = items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false

        self.number_inspections = 0

    def do_round(self):
        copy_items = self.items.copy()
        for item in copy_items:
            item.inspect_item(self.operation)
            self.number_inspections += 1

            self.items.remove(item)

            if self.test(item.worry_level):
                self.true.items.append(item)
            else:
                self.false.items.append(item)
        

    def print(self):
        print('Monkey', self.name + ': ', end='')
        for item in self.items:
            print(item.worry_level, end=' ')
        print()


unparsed_monkeys = []

with open('day11/input.txt') as f:
    current_monkey = []
    line_index = 0
    for line in f:
        if (line != '\n'):
            current_monkey.append(line.strip())
        else:
            unparsed_monkeys.append(current_monkey)
            current_monkey = []
    
    unparsed_monkeys.append(current_monkey)


monkeys = []

def deal_with_monkeys():
    for monkey in unparsed_monkeys:
        parse_input(monkey)

    for monkey, unparsed_monkey in zip(monkeys, unparsed_monkeys):
        add_true_false(monkey, unparsed_monkey[4], unparsed_monkey[5])


op = {'+': lambda x, y: x + y,
      '-': lambda x, y: x - y,
      '*': lambda x, y: x * y,
      '/': lambda x, y: x / y,}

def parse_input(monkey):
    name = monkey[0]
    items = monkey[1]
    operation = monkey[2]
    test = monkey[3]

    items = items.split(': ')[1].split(', ')

    item_list = []

    for item in items:
        item_list.append(Item(int(item)))

    op_value = operation[23:]
    operator = operation[21]

    if op_value == 'old':
        operation = lambda x: op[operator](x, x)
    else:
        operation = lambda x: op[operator](x, int(op_value))

    test_value = test[19:]
    test = lambda x : x % int(test_value) == 0

    monkeys.append(Monkey(name=name.split(' ')[1].split(':')[0], items=item_list, operation=operation, test=test, true=None, false=None))

def add_true_false(monkey, true, false):
    monkey.true = monkeys[int(true[-1])]
    monkey.false = monkeys[int(false[-1])]
    print(true[-1], false[-1])

deal_with_monkeys()
for i in range(10000):
    # print("ROUND ", i+1)
    for monkey in monkeys:
        monkey.do_round()
    
    # for monkey in monkeys:
    #     monkey.print()

    # print('-----')

total = []

for monkey in monkeys:
    total.append(monkey.number_inspections)

total.sort(reverse=True)
print(total)
print(total[0] * total[1])