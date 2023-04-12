import sys
input = sys.stdin.readline


def main():
    n, b = map(int, input().split())
    res = ""

    while n != 0:
        a = n % b
        if a >= 10:
            res += chr(a + 55)
        else:
            res += str(a)
        n //= b

    print(res[::-1])


main()
