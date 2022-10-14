import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

array.sort()

mi = 2000000000
x = 0
y = N - 1
ans = [0, 0]
while x < y:
    result = array[x] + array[y]
    if abs(result) < mi:
        mi = abs(result)
        ans[0] = array[x]
        ans[1] = array[y]
    if result > 0:
        y -= 1
    else:
        x += 1

print(ans[0], ans[1])