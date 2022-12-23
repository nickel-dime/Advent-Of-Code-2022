with open('day6/input.txt') as f:
    data = f.read().replace('\n', '')
    dif = 14

    for i in range(len(data)-dif):
        window = data[i:i+dif]
        # check if string has repeated letters
        if len(window) == len(set(window)):
            print(i+dif)
            break

        
