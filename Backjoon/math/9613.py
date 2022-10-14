import sys, math
from itertools import combinations

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    input_list = list(map(int, input().split()))
    sum_gcd = 0
    for i in combinations(input_list[1:], 2):
        a, b = i
        gcd = math.gcd(a, b)
        sum_gcd += gcd
    print(sum_gcd)