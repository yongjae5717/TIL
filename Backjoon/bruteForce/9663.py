import sys

N = int(sys.stdin.readline())
chess = [0] * N


def check(x, y):
    for i in range(y):
        if chess[i] == x or y - i == x - chess[i] or y - i == chess[i] - x:
            return False
    return True


result = 0


def N_queen(n):
    global result
    if n == N:
        result += 1
    else:
        for i in range(N):
            chess[n] = i
            if check(i, n):
                N_queen(n+1)


N_queen(0)
print(result)