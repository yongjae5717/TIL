import sys
input = sys.stdin.readline


def main():
    n = int(input())
    if n % 2 == 0:
        print("CY")
    else:
        print("SK")


main()