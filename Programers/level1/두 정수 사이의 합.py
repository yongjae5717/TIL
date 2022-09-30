def solution(a, b):
    if a == b:
        return a
    if a < b:
        lst = [i for i in range(a, b + 1)]
        return sum (lst)
    elif a > b:
        lst = [i for i in range(b, a + 1)]
        return sum(lst)