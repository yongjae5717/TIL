import heapq


def solution(scoville, K):
    heap = list()
    for i in scoville:
        heapq.heappush(heap, i)

    answer = 0
    while heap:
        x = heapq.heappop(heap)
        if x >= K:
            heapq.heappush(heap, x)
            return answer
        answer += 1
        if heap:
            y = heapq.heappop(heap)
            temp = x + y * 2
            heapq.heappush(heap, temp)
        else:
            return -1
    return -1