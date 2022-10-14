import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    input_list = list()
    for i in range(N):
        input_list.append(list(map(int, sys.stdin.readline().rstrip())))
    # print(input_list)

    count = 0
    for i in range(N-1):
        for j in range(M-1):

    print(count)


main()