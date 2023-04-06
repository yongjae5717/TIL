import sys
input = sys.stdin.readline


def main():
    A, B, C = map(int, input().split())
    print((A + B) % C, ((A % C) + (B % C)) % C, (A * B) % C, ((A % C) * (B % C)) % C)


main()