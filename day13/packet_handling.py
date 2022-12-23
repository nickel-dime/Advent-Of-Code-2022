import ast

# Packet Packet -> Boolean
def handle_packets(packet1, packet2):
    
    # print(packet1, packet2)

    # cur_index = 0

    # while len(packet1) > cur_index and len(packet2) > cur_index:
    #     print(packet1[cur_index], packet2[cur_index])
    #     cur_index += 1
    #     element1 = packet1[cur_index]
    #     element2 = packet2[cur_index]

    #     if type(element1) == 'int' and type(element2) == 'int':
    #         if element2 > element1:
    #             return False
    #         elif element1 > element2:
    #             return True
    #     elif type(element1) == 'list' and type(element2) == 'list':
    element1 = packet1
    element2 = packet2


    if type(element1) is int and type(element2) is int:
        return element1 - element2
    elif type(element1) is list and type(element2) is list:
        for l, r in zip(element1, element2):
            return_value = handle_packets(l, r)
            if return_value:
                return return_value
            else:
                return len(packet1) - len(packet2)
    elif type(element1) is int and type(element2) is list:
        return handle_packets([element1], element2)
    elif type(element1) is list and type(element2) is int:
        return handle_packets(element1, [element2])
    

total = 0
index = 1

def compair(left, right):
    match left, right:
        case int(), int():
            return left - right
        case list(), list():
            for l, r in zip(left, right):
                if diff := compair(l, r):
                    return diff
            else:
                return len(left) - len(right)
        case int(), list():
            return compair([left], right)
        case list(), int():
            return compair(left, [right])


with open('day13/input.txt') as f:
    for line1, line2 in zip(f, f):
        if compair(ast.literal_eval(line1.strip()), ast.literal_eval(line2.strip())):
            print(index)
            total += index

        next(f, '')
        index += 1

print(total)
