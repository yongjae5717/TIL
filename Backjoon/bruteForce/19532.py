import sys
input = sys.stdin.readline

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        value_1 = a * i + b * j
        value_2 = d * i + e * j
        if value_1 == c and value_2 == f:
            print(i, j)
            break