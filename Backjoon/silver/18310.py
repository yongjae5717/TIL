import sys
input = sys.stdin.readline


def main():
    n = int(input())
    houses = list(map(int, input().split()))
    houses.sort()

    print(houses[(n-1) // 2])


main()