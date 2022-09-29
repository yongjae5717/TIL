import sys
input = sys.stdin.readline


def solution(s):
    answer = ''
    temp = "|"
    for c in s:
        if temp == "|" or temp == " ":
            answer += str(c).upper()
        else:
            answer += str(c).lower()
        temp = c
    return answer


s = input().strip()
print(solution(s))