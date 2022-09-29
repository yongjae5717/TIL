"""
n개의 정수
1. 만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산 (x > 0)
2. x가 0이라면 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거
"""


import sys, heapq
input = sys.stdin.readline

n = int(input())
lst = list()

for _ in range(n):
    x = int(input())
    if x > 0:
        heapq.heappush(lst, x)
    else:
        if len(lst) != 0:
            print(heapq.heappop(lst))
        else:
            print(0)