import sys
input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
t.sort()

result = -1
if n % 2 == 0:
    for i in range(int(n / 2)):
        result = max(result, t[i] + t[len(t)-i-1])
else:
    result = max(result, t.pop())
    for i in range(int(n / 2)):
        result = max(result, t[i] + t[len(t)-i-1])

print(result)