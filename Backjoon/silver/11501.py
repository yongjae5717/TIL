import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stock_of_day = list(map(int, input().split()))
        result, maxValue = 0, 0
        for i in range(n-1, -1, -1):
            if stock_of_day[i] > maxValue:
                maxValue = stock_of_day[i]
            else:
                result += maxValue - stock_of_day[i]
        print(result)


main()