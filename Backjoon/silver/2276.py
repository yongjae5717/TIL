import sys
input = sys.stdin.readline


def binary_search(start, end, target, data):

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return 0


def main():
    t = int(input())
    for _ in range(t):
        note1_n = int(input())
        note1 = list(map(int, input().split()))
        note1.sort()

        note2_n = int(input())
        note2 = list(map(int, input().split()))

        for n in note2:
            print(binary_search(0, note1_n - 1, n, note1))


main()