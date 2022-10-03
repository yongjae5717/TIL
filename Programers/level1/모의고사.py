def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0

    answer = []
    l = len (answers)
    for i in range (l):
        if p1[i % 5] == answers[i]:
            c1 += 1
        if p2[i % 8] == answers[i]:
            c2 += 1
        if p3[i % 10] == answers[i]:
            c3 += 1
    maxValue = max (c1, c2, c3)

    if c1 == maxValue:
        answer.append (1)
    if c2 == maxValue:
        answer.append (2)
    if c3 == maxValue:
        answer.append (3)

    return answer