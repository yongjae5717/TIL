import sys
input = sys.stdin.readline
n, k = map(int, input().split())

result = 0

for i in range(n+1):
    for j in range(60):
        for l in range(60):
            lst = list(str(i) + str(j) + str(l))
            if len(lst) < 6:
                lst.append("0")
            if str(k) in lst:
                result += 1

print(result)