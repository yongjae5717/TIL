import sys
input = sys.stdin.readline


def main():
    n = int(input())
    binList = reversed(bin(n)[2:])
    t, result = 1, 0
    for b in binList:
        result += int(b) * t
        t *= 3
    return result


print(main())