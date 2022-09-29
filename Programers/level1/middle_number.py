"""
s 스트링의 가운데 문자를 반환
홀수: 가운데 반환
짝수: 가운데 + 1
"""
import sys
input = sys.stdin.readline


def solution(s):
    length = len(s)
    if length % 2 == 0:
        return s[length//2 - 1] + s[length//2]
    else:
        return s[length//2]


s = input().strip()
print(solution(s))