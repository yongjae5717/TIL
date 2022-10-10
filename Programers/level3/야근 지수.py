import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    temp = []
    for i in works:
        heapq.heappush(temp, -i)

    for _ in range(n):
        heapq.heappush(temp, heapq.heappop(temp)+1)

    answer = 0
    for i in temp:
        answer += (-i) ** 2
    return answer