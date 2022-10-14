import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
result = list()
for i in range(1, N + 1):
    temp = list(combinations(array, i))
    for j in range(len(temp)):
        result.append(sum(temp[j]))

count = 0
for k in range(len(result)):
    if result[k] == S:
        count += 1
print(count)