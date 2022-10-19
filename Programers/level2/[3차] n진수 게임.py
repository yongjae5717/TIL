"""
n: 진법
t: 미리 구할 숫자의 갯수
m: 게임에 참가하는 인원
p: 튜브의 순서
"""


def function(n, base):
    sixteen_number = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return sixteen_number[r]
    else:
        return function(q, base) + sixteen_number[r]


def solution(n, t, m, p):
    answer, temp = '', ''
    for i in range(m*t):
        temp += str(function(i, n))

    while len(answer) < t:
        answer += temp[p-1]
        p += m
    return answer


print(solution(2, 4, 2, 1))

print(solution(16, 16, 2, 1))