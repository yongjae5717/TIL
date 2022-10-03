def solution(a, b):
    lst = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    m, d = a - 1, b - 1

    s = sum (lst[:m]) + d

    return day[s % 7]