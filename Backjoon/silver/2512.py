import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    m = int(input())

    start, end = 0, max(lst)

    while start <= end:
        mid = (start + end) // 2
        total_budget = 0
        for i in lst:
            if i >= mid:
                total_budget += mid
            else:
                total_budget += i
        if total_budget <= m:
            start = mid + 1
        else:
            end = mid - 1
    print(end)


main()