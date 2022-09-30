def solution(n):
    temp = str(n)
    answer = []
    for i in range(len(temp)):
        answer.append(int(temp[len(temp)-i-1]))
    return answer