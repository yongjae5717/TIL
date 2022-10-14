import sys, math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    gcd = math.gcd(a, b)
    print(a * b // gcd)