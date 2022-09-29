"""
n = 10000이하의 자연수
n이 들어가면 '수, 박, 수, 박'이 출력
"""
import sys
input = sys.stdin.readline


def solution(n):
    answer = ""
    temp = n
    if n % 2 == 0:
        inp1 = "수"
        inp2 = "박"
    else:
        inp1 = "박"
        inp2 = "수"
    for i in range(n):
        if temp % 2 == 0:
            answer += inp1
        else:
            answer += inp2
        temp -= 1
    return answer


N = int(input())
print(solution(N))