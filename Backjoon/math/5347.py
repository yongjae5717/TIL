import sys, math
input = sys.stdin.readline

n = int(input())
for _ in range(n):

    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    print(a * b // gcd)
