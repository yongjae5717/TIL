import sys, math
input = sys.stdin.readline


def is_prime_number(number):
    if number <= 1:
        return False

    if number % 2 == 0:
        if number == 2:
            return True
        return False

    for i in range(3, int(pow(number, 0.5)) + 1, 2):
        if number % i == 0:
            return False
    return True


t = int(input())
for _ in range(t):
    n = int(input())

    while True:
        if is_prime_number(n):
            print(n)
            break
        else:
            n += 1