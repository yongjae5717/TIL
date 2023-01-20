import sys
input = sys.stdin.readline


def main():
    n1, n2 = map(int, input().split())
    set1 = set(map(int, input().split()))
    set2 = set(map(int, input().split()))

    set3 = list(set1 - set2)
    set3.sort()

    print(len(set3))
    if set3:
        print(*set3)


main()