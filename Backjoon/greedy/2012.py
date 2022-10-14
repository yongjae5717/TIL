import sys

N = int(sys.stdin.readline())
array = [int(sys.stdin.readline().strip()) for _ in range(N)]
array.sort()

result = 0

for i in range(1, N + 1):
    result += abs(array[i-1] - i)

print(result)