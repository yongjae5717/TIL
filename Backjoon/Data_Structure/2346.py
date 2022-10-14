import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
balloons = deque(enumerate(map(int, input().split())))
result = list()

while balloons:
    x, value = balloons.popleft()
    result.append(x+1)

    if value > 0:
        for _ in range(value-1):
            if len(balloons) != 0:
                balloons.append(balloons.popleft())
    else:
        for _ in range(abs(value)):
            if len(balloons) != 0:
                balloons.appendleft(balloons.pop())

print(*result)