import sys

M = int(sys.stdin.readline())
lst = set()
for i in range(M):
    temp = sys.stdin.readline().split()

    function = temp[0]
    num = 0

    if len(temp) == 2:
        num = int(temp[1])

    if function == "add":
        lst.add(num)
    elif function == "remove":
        lst.discard(num)
    elif function == "check":
        if num in lst:
            print(1)
        else:
            print(0)
    elif function == "toggle":
        if num in lst:
            lst.discard(num)
        else:
            lst.add(num)
    elif function == "all":
        lst = set([i for i in range(1, 21)])
    elif function == "empty":
        lst.clear()