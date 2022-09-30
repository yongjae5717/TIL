def solution(n):
    lst = list(str(n))
    lst.sort(reverse=True)

    return int("".join(lst))