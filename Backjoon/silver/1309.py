import sys
input = sys.stdin.readline


def main():
    n = int(input())
    dp = list([0, 0, 0] for _ in range(n+1))

    dp[1] = [1, 1, 1]

    for i in range(2, n + 1):
        not_selection = dp[i-1][0] + dp[i-1][1] + dp[i-1][2]
        left_selection = dp[i-1][0] + dp[i-1][2]
        right_selection = dp[i-1][0] + dp[i-1][1]
        dp[i] = [not_selection % 9901, left_selection % 9901, right_selection % 9901]

    print(sum(dp[n]) % 9901)


main()