import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

lst = list(permutations(list(i for i in range(1, n+1)), n))

for j in lst:
    print(*j)