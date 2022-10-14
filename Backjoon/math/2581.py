import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

dp = [True for _ in range(n+1)]

for i in range(2, n+1):
    if dp[i]:
        j = 2
        while i * j <= n:
            dp[i * j] = False
            j += 1


result = list()
for i in range(m, n+1):
    if dp[i] is True and i != 1:
        result.append(i)


if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)