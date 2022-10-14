import sys

T = int(sys.stdin.readline())
ans = []

for i in range(T):
    result = []
    N = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    array.sort()

    for j in range(2, N):
        result.append(array[j] - array[j-2])
    ans.append(max(result))

for k in ans:
    print(k)