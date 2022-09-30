def solution(x, n):
    temp = 0
    answer = list()
    while n != 0:
        temp += x
        answer.append(temp)
        n -= 1
    return answer