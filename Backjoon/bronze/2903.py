import sys
input = sys.stdin.readline


def main():
    n = int(input())
    sequence = 2 ** n + 1
    print(sequence ** 2)


main()