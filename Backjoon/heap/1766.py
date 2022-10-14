import sys, heapq

# N개의 문제는 모두 풀어야한다
# 먼저 푸는 것이 좋은 문제가 있는 문제는,
# 먼저 푸는 것이 좋은 문제를 반드시 먼저 푼다
# 가능하면 쉬운 문제부터 풀어야 한다

# A는 B보다 먼저 푸는 것이 좋다.
N, M = map(int, sys.stdin.readline().split())
q, t = list(), list()
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    heapq.heappush(q, A)
    heapq.heappush(t, B)

result = ""
for i in range(M):
    result += str(heapq.heappop(q)) + " "
    result += str(heapq.heappop(t)) + " "

print(result)