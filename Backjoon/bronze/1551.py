import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    array = list(map(int, input().strip().split(',')))
    for _ in range(k):
        array = transform(array)

    for i in range(len(array)):
        array[i] = str(array[i])
    print(",".join(array))


def transform(lst):
    return list(lst[i]-lst[i-1] for i in range(1, len(lst)))


main()