import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [True for _ in range(n+1)]
dp[1] = False

count = 0
# 1은 소수가 아니기 때문에 제외
for i in range(2, n+1):
    if dp[i]:
        j = 1
        while i * j <= n:
            if dp[i * j]:
                dp[i * j] = False
                count += 1
            if count == k:
                print(i * j)
                break
            j += 1