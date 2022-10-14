import sys

N, L = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

H.sort()

for fruit in H:
    if L >= fruit:
        L += 1
print(L)