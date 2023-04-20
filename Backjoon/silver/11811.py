import sys
input = sys.stdin.readline


def main():
    n = int(input())
    a = [0] * n
    for i in range(n):
        m = list(map(int, input().split()))
        for j in range(n):
            if i == j:
                continue
            a[i] = a[i] | m[j]

    print(*a)


main()