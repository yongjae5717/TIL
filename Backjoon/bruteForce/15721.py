import sys
input = sys.stdin.readline

# n-1회차: ‘뻔 – 데기 – 뻔 – 데기 – 뻔(x n번) – 데기(x n번)’

a = int(input())
t = int(input())
ans = int(input())  # 뻔: 0, "데기: 1

n, count, result = 1, 0, 0
lst = list()
idx = [i for i in range(a)]
while True:
    lst = lst + [0] + [1] + [0] + [1] + [0] * (n+1) + [1] * (n+1)

    if len(lst) // 2 >= t:
        for i in lst:
            result += 1
            if i == ans:
                count += 1
                if count == t:
                    break
        if count == t:
            break
    else:
        n += 1

print(idx[result % a - 1])