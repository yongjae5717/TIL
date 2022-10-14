import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1]

for i in range(2, n+1):
    temp = pow(50000, 2) * 4 + 1
    count = 1
    while pow(count, 2) <= i:
        temp = min(temp, dp[i-pow(count, 2)])
        count += 1

    dp.append(temp + 1)

print(dp[n])