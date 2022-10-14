import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
colors = deque(input().strip())
result_colors = list()
primary_color = ""

while colors:
    x = colors.popleft()
    if x != primary_color:
        result_colors.append(x)
    primary_color = x

if result_colors.count('B') >= result_colors.count('R'):
    result = 1 + result_colors.count('R')
else:
    result = 1 + result_colors.count('B')

print(result)