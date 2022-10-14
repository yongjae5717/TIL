import sys, math
input = sys.stdin.readline

a, b = map(int, input().split())

# Greatest Common Factor
gcd = math.gcd(a, b)
print(gcd)

# Least Common Multiple
print(a * b // gcd)