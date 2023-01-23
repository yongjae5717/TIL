import sys
input = sys.stdin.readline


def main():
    n = int(input())
    assignments = list(list(map(int, input().split())) for _ in range(n))
    assignments.sort(reverse=True, key=lambda x: x[1])
    visited = [0] * 1001
    score = 0

    for d, s in assignments:
        i = d
        while i > 0 and visited[i] != 0:
            i -= 1

        if i != 0:
            visited[i] = 1
            score += s

    print(score)


main()