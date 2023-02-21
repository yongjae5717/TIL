def solution(x, y, n):
    res = 0
    lst = list()
    lst.append(x)
    while lst:
        temp = set()
        if y in lst:
            return res
        if min(lst) > y:
            return -1

        res += 1
        for i in lst:
            temp.add (func1(i,n))
            temp.add (func2(i))
            temp.add (func3(i))

        lst = list(temp)


def func1(x, n):
    return x + n


def func2(x):
    return x * 2


def func3(x):
    return x * 2

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))