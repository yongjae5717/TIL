def solution(n, m):
    # GCD
    x, y = n, m
    while(y):
        x, y = y, x%y
    # LCM
    return[x, int(n * m / x)]