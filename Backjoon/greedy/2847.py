import sys


def main():
    N = int(sys.stdin.readline())
    level = list()
    for _ in range(N):
        level.append(int(sys.stdin.readline()))
    # print(level)

    level.reverse()

    # print(level)
    result_list = list()
    for i in range(1, N):
        if level[i-1] <= level[i]:
            temp = level[i] - level[i-1] + 1
            level[i] = level[i] - temp
            result_list.append(temp)
    print(sum(result_list))




main()