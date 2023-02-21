def solution(x, y, n):
    lst = list()
    lst.append([x, 0])
    res = 1000001
    while lst:
        x, count = lst.pop()
        if x < y:
            temp1 = func1(x, n, count)
            temp2 = func2(x, count)
            temp3 = func3(x, count)
            if temp1[0] <= y:
                lst.append(temp1)
            if temp2[0] <= y:
                lst.append(temp2)
            if temp3[0] <= y:
                lst.append(temp3)
        elif x == y:
            res = min(res, count)

    if res == 1000001:
        return -1
    return res


def func1(x, n, c):
    return [x + n, c + 1]


def func2(x, c):
    return [x * 2, c + 1]


def func3(x, c):
    return [x * 2, c + 1]


print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))
