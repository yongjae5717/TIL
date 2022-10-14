import sys
input = sys.stdin.readline


def tip(money, idx):
    return money - (idx - 1)


n = int(input())
lst = list(int(input()) for _ in range(n))
lst.sort(reverse=True)
result = 0

for i in range(n):
    t = tip(lst[i], i+1)
    if t >= 0:
        result += t

print(result)