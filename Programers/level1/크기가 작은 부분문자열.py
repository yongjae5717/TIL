def solution(t, p):
    answer = 0
    length, standard = len(p), int(p)
    for i in range(len(t)-length+1):
        if int(t[i:i+length]) <= standard:
            answer += 1
    return answer


print(solution("3141592", "271"))