import heapq


def solution(k, score):
    lst = list()
    result = list()
    for s in score:
        if len(lst) < k:
            heapq.heappush(lst, s)
            result.append(lst[0])
        elif len(lst) == k:
            if lst[0] <= s:
                heapq.heappop (lst)
                heapq.heappush(lst, s)
                result.append(lst[0])
            else:
                result.append(lst[0])
    return result


print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))