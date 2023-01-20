import sys
input = sys.stdin.readline


def main():
    n, m, r = map(int, input().split())
    graph = list(list() for _ in range(n+1))
    visited = [0] * (n+1)
    answer = [0] * (n+1)
    count = 1
    stack = list()

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    for i in range(1, n+1):
        graph[i].sort()

    stack.append(r)

    while stack:
        cur_node = stack.pop()
        visited[cur_node] = 1
        if answer[cur_node] == 0:
            answer[cur_node] = count
            count += 1

        for next_node in graph[cur_node]:
            if visited[next_node] == 0:
                stack.append(next_node)

    print(* answer[1:])


main()