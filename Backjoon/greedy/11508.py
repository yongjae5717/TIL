import sys
input = sys.stdin.readline

n = int(input())
C = list(int(input()) for _ in range(n))
C.sort()
result = 0
count = 0
while C:
    count += 1
    x = C.pop()
    if count % 3 != 0:
        result += x

print(result)