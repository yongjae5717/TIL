import sys

N = int(sys.stdin.readline())
non = " "
star = "*"
for i in range(1, N + 1):
    temp = non * (N - i) + star * i
    print(temp)
for i in range(1, N):
    temp = non * i + star * (N - i)
    print(temp)