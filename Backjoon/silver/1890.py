import sys
input = sys.stdin.readline


def main():
    n = int(input())
    board = list(list(map(int, input().split())) for _ in range(n))
    dp = list([0] * (n+1) for _ in range(n+1))
    dp[1][1] = 1

    for i in range(1, n+1):
        for j in range(1, n+1):

            if i == n and j == n:
                break

            jump = board[i-1][j-1]
            if i + jump <= n:
                dp[i + jump][j] += dp[i][j]

            if j + jump <= n:
                dp[i][j + jump] += dp[i][j]

    print(dp[n][n])


main()