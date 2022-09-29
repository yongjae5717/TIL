"""
조건
1. 1부터 N까지 자연수 중 중복없이 M개 고른 수열
2. 고른 수열은 오름차순
"""

import sys
import itertools

input = sys.stdin.readline

n, m = map(int, input().split())
num = list(i for i in range(1, n + 1))

for lst in itertools.combinations(num, m):
    print(*lst)