import itertools
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

cards = list(map(int, input().split()))
result = 0

for i in itertools.combinations(cards, 3):
    if sum(i) <= m:
        result = max(result, sum(i))

print(result)