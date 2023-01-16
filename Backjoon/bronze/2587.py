import sys
input = sys.stdin.readline


def main():
    number = list(int(input()) for _ in range(5))
    number.sort()

    print(sum(number) // 5)
    print(number[2])


main()