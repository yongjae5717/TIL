import sys
input = sys.stdin.readline


def main():
    n = int(input())
    number = list(int(input()) for _ in range(n))
    number.sort(reverse=True)
    for i in range(n):
        print(number[i])


main()