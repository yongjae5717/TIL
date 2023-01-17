import sys
input = sys.stdin.readline


def main():
    n = int(input())
    array = list(map(int, input().split()))
    sorted_array = list(array)
    sorted_array.sort()

    P = list()
    for i in array:
        P.append(sorted_array.index(i))
        sorted_array[sorted_array.index(i)] = -1

    print(* P)


main()