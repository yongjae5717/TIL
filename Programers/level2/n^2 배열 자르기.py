def solution(n, left, right):
    lst = list()
    for i in range(left, right+1):
        lst.append(max(i//n + 1, i % n + 1))
    return lst

print(solution(4, 7, 14))