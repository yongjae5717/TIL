def solution(k, m, score):
    lst = score
    lst.sort(reverse=True)
    result = 0
    for i in range(len(score)):
        if (i+1) % m == 0:
            result += score[i] * m
    return result

    print(lst)
    result = 0
    box = 0
    temp = list()
    while lst:
        temp.append(lst.pop(0))
        if len(temp) == m:
            box += 1
            minScore = min(min(temp), k)
            result += minScore * m
            temp = list()
    return result



print(solution(3, 4, [1, 2, 3, 1, 2, 3, 1]))
print(solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))