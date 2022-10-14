import sys


def main():
    N = int(sys.stdin.readline())
    case = list()
    money = [25, 10, 5, 1]
    C = 0
    result = ""
    for _ in range(N):
        C = int(sys.stdin.readline())
        for i in range(len(money)):
            result += str(C // money[i]) + " "
            # case.append(C // money[i])
            C = C - (C // money[i]) * money[i]
        result += "\n"
    print(result)


main()