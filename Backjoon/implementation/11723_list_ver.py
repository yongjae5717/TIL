import sys

M = int(sys.stdin.readline())
lst = list([0] * 20)
for i in range(M):
    temp = sys.stdin.readline().split()
    function = temp[0]
    num = 0
    if len(temp) == 2:
        num = int(temp[1])
    if function == "add":
        lst[num-1] = 1
    elif function == "remove":
        lst[num-1] = 0
    elif function == "check":
        if lst[num-1] == 1:
            print(1)
        else:
            print(0)
    elif function == "toggle":
        if lst[num-1] == 1:
            lst[num-1] = 0
        else:
            lst[num-1] = 1
    elif function == "all":
        for j in range(20):
            lst[j] = 1
    elif function == "empty":
        for j in range(20):
            lst[j] = 0