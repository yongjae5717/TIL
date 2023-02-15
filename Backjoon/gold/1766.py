import sys, heapq
input = sys.stdin.readline


def main():
    n, m = map(int, input().split())
    res = list()
    graph = list(list() for _ in range(n+1))
    in_degree = [0] * (n+1)
    q = list()

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_degree[b] += 1

    for i in range(1, n+1):
        if in_degree[i] == 0:
            heapq.heappush(q, i)

    while q:
        lst = heapq.heappop(q)
        res.append(lst)
        for i in graph[lst]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                heapq.heappush(q, i)
    print(* res)


main()