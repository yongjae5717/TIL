"""
조건: 키, 몸무게 (x, y)
둘다 커야 덩치가 크다.
"""

import sys
input = sys.stdin.readline

n = int(input())
array = list(list(map(int, input().split())) for _ in range(n))

result = list()
for i in array:
    x, y = i
    count = 1
    for j in array:
        p, q = j
        if x < p and y < q:
            count += 1

    result.append(count)

print(*result)