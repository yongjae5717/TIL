import sys
input = sys.stdin.readline

n = int(input())

i = 2
while n != 1:
    if n % i == 0:
        n /= i
        print(i)
        i = 2
    else:
        i += 1