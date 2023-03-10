import sys, math
input = sys.stdin.readline


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a, b = n // 2, n // 2
        while a > 0:
            if is_prime(a) and is_prime(b):
                print(a, b)
                break
            else:
                a -= 1
                b += 1


def is_prime(num):
    if num == 1:
        return False
    if num % 2 == 0:
        if num == 2:
            return True
        return False
    for i in range (3, int (math.sqrt (num)) + 1):
        if num % i == 0:
            return False
    return True


main()