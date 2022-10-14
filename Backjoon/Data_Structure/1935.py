import sys
from collections import deque
input = sys.stdin.readline

# 1 + 2 * 3 - 4 / 5 = 7 - 0.8 = 6.2

n = int(input())
input_string = list(input().strip())
list_num = [0] * n
for i in range(n):
    list_num[i] = int(input())

stack = deque()

for i in input_string:
    if 'A' <= i <= 'Z':
        stack.append(list_num[ord(i) - ord('A')])
    else:
        element1, element2 = 0, 0
        if len(stack) != 0:
            element2 = stack.pop()
            element1 = stack.pop()
        if i == '+':
            stack.append(element1 + element2)
        elif i == '-':
            stack.append(element1 - element2)
        elif i == '/':
            stack.append(element1 / element2)
        elif i == '*':
            stack.append(element1 * element2)

print(format(*stack, ".2f"))
