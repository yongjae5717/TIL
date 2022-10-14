import sys
import heapq


def main():
    N = int(sys.stdin.readline())
    plus_array = list()
    minus_array = list()
    flag = 0
    if N == 1:
        index = int(sys.stdin.readline())
        print(index)
    else:
        for _ in range(N):
            index = int(sys.stdin.readline())
            if index > 0:
                heapq.heappush(plus_array, index)
            elif index < 0:
                heapq.heappush(minus_array, index)
            else:
                flag = 1
    plus_array.sort(reverse=True)
    minus_array.sort()

    result_array = list()

    if len(plus_array) == 1:
        t = heapq.heappop(plus_array)
        heapq.heappush(result_array, t)
    else:
        for i in range(len(plus_array) // 2):
            temp1 = heapq.heappop(plus_array)
            plus_array.sort(reverse=True)
            temp2 = heapq.heappop(plus_array)
            plus_array.sort(reverse=True)
            # print(temp1, temp2)
            if temp1 + temp2 > temp1 * temp2:
                heapq.heappush(result_array, temp1 + temp2)
            else:
                heapq.heappush(result_array, temp1 * temp2)
        if len(plus_array) % 2 != 0:
            t = heapq.heappop(plus_array)
            heapq.heappush(result_array, t)

    if len(minus_array) == 1 and flag == 1:
        t = heapq.heappop(minus_array)
        heapq.heappush(result_array, 0)
    else:
        if flag == 1 and len(minus_array) > 0 and len(minus_array) % 2 == 1:
            minus_array.sort(reverse=True)
            t = heapq.heappop(minus_array)
            minus_array.sort()
            heapq.heappush(result_array, 0)
        for i in range(len(minus_array) // 2):
            temp1 = heapq.heappop(minus_array)
            minus_array.sort()
            temp2 = heapq.heappop(minus_array)
            minus_array.sort()
            # print(temp1, temp2)
            if temp1 + temp2 > temp1 * temp2:
                heapq.heappush(result_array, temp1 + temp2)
            else:
                heapq.heappush(result_array, temp1 * temp2)
        if len(minus_array) % 2 != 0:
            t = heapq.heappop(minus_array)
            heapq.heappush(result_array, t)

    if N != 1:
        print(sum(result_array))


main()