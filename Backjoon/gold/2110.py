import sys
input = sys.stdin.readline


def solution(n, c, positions):
    result = 0
    start, end = 1, positions[-1] - positions[0]

    while start <= end:
        mid = (start + end) // 2
        now = positions[0]
        count = 1

        for i in range(1, n):
            if positions[i] >= now + mid:
                count += 1
                now = positions[i]

        if count >= c:
            start = mid + 1
            result = mid
        else:
            end = mid - 1
    return result


def main():
    n, c = map(int, input().split())
    positions = list(int(input()) for _ in range(n))
    positions.sort()
    print(solution(n, c, positions))


main()