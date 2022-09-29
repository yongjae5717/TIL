"""
10,000 이하의 자연수로 이루어진 길이 N짜리 수열
조건
1. 연속된 수들의 부분합 중 합이 S이상 되는 것
2. 가장 짧은 것의 길이를 구하라
범위
N: 10 ~ 100,000
S: 0 ~ 100,000,000
각 수열의 원소: 10000이하의 자연수
출력
구하자고 하는 최소의 길이
불가능하다면 0 출력
"""

import sys
input = sys.stdin.readline

n, s = map(int, input().split())
array = list(map(int, input().split()))

sumValue, start, end = array[0], 0, 0
result = 100001  # 최대 길이가 100,000

while True:
    if sumValue >= s:
        sumValue -= array[start]
        result = min(result, end - start + 1)
        start += 1
    else:
        end += 1
        if end == n:
            break
        sumValue += array[end]

if result == 100001:
    print(0)
else:
    print(result)