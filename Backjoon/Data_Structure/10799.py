import sys
from collections import deque
input = sys.stdin.readline

input_string = deque(input().strip())
count = 0
result = 0
primary_string = ""
while len(input_string) != 0:
    temp = input_string.pop()
    if temp == ")":
        count += 1
    else:
        if primary_string == "(":
            count -= 1
            result += 1
        else:
            count -= 1
            result += count

    primary_string = temp

print(result)