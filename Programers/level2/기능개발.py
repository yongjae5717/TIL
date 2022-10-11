def solution(progresses, speeds):
    lst = dict()
    day = 0
    for p, s in zip(progresses, speeds):
        p = p + s * day
        while p < 100:
            p += s
            day += 1
        if day not in lst:
            lst[day] = 1
        else:
            lst[day] += 1

    answer = list(i for i in lst.values())
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
