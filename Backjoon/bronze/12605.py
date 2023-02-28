import sys
input = sys.stdin.readline


def main():
    n = int(input())
    for i in range(1, n+1):
        lst = list(reversed(list(input().split())))
        print(f'Case #{i}: {" ".join(lst)}')


main()