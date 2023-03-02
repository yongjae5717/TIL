import sys
input = sys.stdin.readline


def main():
    n = int(input())
    time = list(list(map(int, input().split())) for _ in range(n))
    time.sort(key=lambda x: (x[0], -x[1]))
    current_time = 0
    for t in time:
        current_time = after_time(t, current_time)
    print(current_time)


def after_time(time, current_time):
    start, period = time
    if start >= current_time:
        return start + period
    return current_time + period


main()