import sys
input = sys.stdin.readline


def main():
    a, b, v = map(int, input().split())
    result = v - a - 1
    value = a - b
    print(result // value + 2)


main()