import math


def solution(arr):
    first = 1
    while arr:
        second = arr.pop()
        first = lcd(first, second)
    return first


def lcd(x, y):
    gcd = math.gcd(x, y)
    return int(x * y / gcd)