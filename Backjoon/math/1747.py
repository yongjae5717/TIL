import sys, math
input = sys.stdin.readline


def is_prime(num):
    if num == 1:
        return False
    if num % 2 == 0:
        if num == 2:
            return True
        return False
    for i in range(3, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def is_pal(num):
    s = str(num)
    for i in range(len(s) // 2):
        if s[i] != s[len(s)-1 -i]:
            return False
    return True


n = int(input())
while True:
    if is_prime(n) and is_pal(n):
        print(n)
        break
    n += 1