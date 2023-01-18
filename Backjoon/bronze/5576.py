import sys
input = sys.stdin.readline


def main():
    w = list(int(input()) for _ in range(10))
    k = list(int(input()) for _ in range(10))
    w.sort(reverse=True)
    k.sort(reverse=True)
    print(sum(w[:3]), sum(k[:3]))


main()