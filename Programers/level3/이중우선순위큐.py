import heapq


def solution(operations):
    q = list()
    max_q = list()
    for o in operations:
        command, number = o.split()
        number = int(number)
        if command == "I":
            heapq.heappush(q, number)
            heapq.heappush(max_q, -number)
        elif command == "D":
            if len(q) == 0:
                continue
            if number == 1:
                max_value = -heapq.heappop(max_q)
                q.remove(max_value)
            elif number == -1:
                min_value = heapq.heappop(q)
                max_q.remove(-min_value)
    if q:
        return [-heapq.heappop(max_q), heapq.heappop(q)]
    else:
        return [0, 0]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))