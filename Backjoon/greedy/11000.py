import sys
import heapq


def main():
    N = int(sys.stdin.readline())
    SiTi = list()

    for _ in range(N):
        S, T = map(int, sys.stdin.readline().split())
        SiTi.append((S, T))
    SiTi.sort()
    print(SiTi)

    room = list()
    heapq.heappush(room, SiTi[0][1])

    for i in range(1, N):
        Si, Ti = SiTi[i]
        if Si < room[0]:
            heapq.heappush(room, Ti)
        else:
            heapq.heappop(room)
            heapq.heappush(room, Ti)
    print(len(room))


main()