import sys, heapq
from collections import defaultdict
input = sys.stdin.readline
heap_min = list()
heap_max = list()
dp = defaultdict(bool)


def main():
    n = int(input())
    for _ in range(n):
        p, l = map(int, input().split())
        heapq.heappush(heap_min, (l, p))
        heapq.heappush(heap_max, (-l, -p))
        dp[p] = True

    m = int(input())
    for _ in range(m):
        tmp = list(input().split())
        if tmp[0] == "recommend":
            recommend(int(tmp[1]))
        elif tmp[0] == "add":
            add(int(tmp[1]), int(tmp[2]))
        elif tmp[0] == "solved":
            solved(int(tmp[1]))


def solved(p):
    dp[p] = False


def add(p, l):
    while not dp[-heap_max[0][1]]:
        heapq.heappop(heap_max)
    while not dp[heap_min[0][1]]:
        heapq.heappop(heap_min)
    heapq.heappush (heap_min, (l, p))
    heapq.heappush (heap_max, (-l, -p))
    dp[p] = True


def recommend(x):
    if x == 1:
        while not dp[-heap_max[0][1]]:
            heapq.heappop(heap_max)
        print(-heap_max[0][1])
    elif x == -1:
        while not dp[heap_min[0][1]]:
            heapq.heappop(heap_min)
        print(heap_min[0][1])


main()