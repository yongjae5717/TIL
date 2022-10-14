import sys


def main():
    docu = list(map(str, sys.stdin.readline().rstrip()))
    find = sys.stdin.readline().rstrip()
    # print(docu, find)

    count = 0
    first, second = -1, -1
    for i in range(len(docu) - len(find) + 1):
        temp = ""
        for j in range(len(find)):
            temp += docu[j+i]
            if temp == find and first == -1:
                # print(temp, i, i + j)
                first = i
                second = i + j
                count += 1
                temp = ""
            elif temp == find and i > second:
                first = i
                second = i + j
                # print(temp, i, i + j, second)
                count += 1
                temp = ""

    print(count)


main()
