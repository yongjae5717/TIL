import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        i = 1
        while n != 1:
            i += 1
            count = 0
            if n % i == 0:
                while n % i == 0:
                    n //= i
                    count += 1
                print(i, count)


main()