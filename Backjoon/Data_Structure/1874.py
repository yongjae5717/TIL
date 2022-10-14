import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque(i for i in range(1, n+1))
stack2 = deque()
primary_num = 0
flag = False
result = list()

for _ in range(n):
    input_number = int(input())
    temp = 0

    if primary_num < input_number:
        flag = False
    else:
        flag = True

    while True:
        if temp != input_number and flag is False:
            if len(stack) != 0:
                temp = stack.popleft()
            else:
                result.append("NO")
                break
            stack2.appendleft(temp)
            result.append("+")
        else:
            temp = stack2.popleft()
            if temp == input_number:
                result.append("-")
            else:
                result.append("NO")
            break
    primary_num = input_number

if result[len(result)-1] == "NO":
    print("NO")
else:
    for i in result:
        print(i)