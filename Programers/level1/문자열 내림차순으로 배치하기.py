def solution(s):
    lst = list(s)
    lst.sort(reverse=True)
    return "".join(lst)