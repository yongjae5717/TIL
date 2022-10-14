import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
if n == 1:
    print(int(input()))
else:
    lst = list(map(int, input().split()))
    lst.sort()
    for i in product(lst, repeat=m):
        print(*i)