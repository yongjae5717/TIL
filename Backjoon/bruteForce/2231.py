import sys

N = sys.stdin.readline().strip()
len_N = len(N)
N = int(N)
result_list = list()
out = N


def function(N):
    for i in range(N):
        number = str(i)
        result = ""
        s = 0
        for i in number:
            result += i
            s += int(i)
        ans = int(result) + s
        if ans == out:
            return int(result)


if function(N):
    print(function(N))
else:
    print(0)