import sys

M = int(sys.stdin.readline())
dictionary = dict()
for i in range(M):
    temp = sys.stdin.readline().split()
    function = temp[0]
    number = 0
    if len(temp) == 2:
        number = int(temp[1])
    if function == 'add':
        if number not in dictionary:
            dictionary[number] = 1
    elif function == 'check':
        if number in dictionary and dictionary[number] == 1:
            print(1)
        else:
            print(0)
    elif function == "remove":
        if number in dictionary:
            dictionary[number] = 0
    elif function == "toggle":
        if number not in dictionary:
            dictionary[number] = 0
        if dictionary[number] == 1:
            dictionary[number] = 0
        elif dictionary[number] == 0:
            dictionary[number] = 1
    elif function == "all":
        for i in range(1, 21):
            if i not in dictionary:
                dictionary[i] = 1
            elif i in dictionary:
                dictionary[i] = 1
    elif function == "empty":
        for i in dictionary:
            dictionary[i] = 0