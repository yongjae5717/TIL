"""
N: 온도를 측정한 전체 날짜의 수
K: 합을 구하기 위한 연속적인 날짜의 수
구하고자 하는 것: K일 동안의 온도의 합이 가장 큰 프로그램을 계산하는 프로그램
"""

import sys

N, K = map(int, sys.stdin.readline().split())

lst = list(map(int, sys.stdin.readline().split()))
# N-K+1는 K일동안 온도의 합을 구하는 집합의 원소의 개수


result = sum(lst[0:K])
ans = result
for i in range(1, N-K+1):
    result = result - lst[i-1] + lst[i+K-1]
    if ans < result:
        ans = result

print(ans)