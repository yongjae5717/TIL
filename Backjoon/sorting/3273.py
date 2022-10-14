import sys
import heapq

N = int(sys.stdin.readline())
array = sorted(list(map(int, sys.stdin.readline().split())))
X = int(sys.stdin.readline())
result = 0
plus = 0
i, j = 0, N-1

while i < j:
    plus = array[i] + array[j]
    if plus < X:
        i += 1
        continue
    elif plus == X:
        result += 1
        # print(array[i], array[j])
    j -= 1
print(result)