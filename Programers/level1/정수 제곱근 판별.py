from math import sqrt


def solution(n):
    temp = int(sqrt(n))
    for i in range(1, temp + 1):
        if n == pow(i, 2):
            return pow(i+1, 2)
    return -1
