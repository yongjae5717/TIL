import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
lst = deque(i for i in range(1, N+1))
result = list()

count = 0
while len(lst) != 0:
    count += 1
    if count % K != 0:
        lst.append(lst.popleft())
    else:
        result.append(lst.popleft())

ans = "<"
for i in result:
    ans += str(i) + ", "

print(ans[:-2] + ">")