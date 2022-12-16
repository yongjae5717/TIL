import sys
input = sys.stdin.readline


def solution():
    m, n = map(int, input().split())
    result = list()
    for i in range(m, n + 1):
        if i == 1:
            continue

        prime = True
        for j in range(2, int(int(i) ** 0.5) + 1):
            if int(i) % j == 0:
                prime = False
                break
        if prime:
            result.append(i)
    return result


for r in solution():
    print(r)