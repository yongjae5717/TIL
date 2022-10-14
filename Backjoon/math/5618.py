import sys
import math
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

# greatest common factor
gcf = math.gcd(*n_list)

for i in range(1, gcf+1):
    if gcf % i == 0:
        print(i)