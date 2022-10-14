import sys
import heapq


def main():
    N, K = map(int, sys.stdin.readline().split())
    weight_price_list = list()
    bag_list = list()
    cap = list()

    for _ in range(N):
        weight, price = map(int, sys.stdin.readline().split())
        heapq.heappush(weight_price_list, (weight, price))

    for _ in range(K):
        bag = int(input())
        heapq.heappush(bag_list, bag)

    # print(weight_price_list)
    # print(bag_list)

    result = 0

    for _ in range(K):
        # print("weight_price_list:", weight_price_list)
        # print("bag_list:", bag_list)
        bag = heapq.heappop(bag_list)
        while weight_price_list and bag >= weight_price_list[0][0]:
            weight, price = heapq.heappop(weight_price_list)
            heapq.heappush(cap, -price)
            # print("cap:", cap)

        if cap:
            result -= heapq.heappop(cap)
        elif not weight_price_list:
            break

    print(result)


main()