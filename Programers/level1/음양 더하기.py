def solution(absolutes, signs):
    answer = 0
    for x, y in zip (absolutes, signs):
        if y:
            answer += x
        else:
            answer -= x
    return answer
