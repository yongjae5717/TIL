import sys
input = sys.stdin.readline


def main():
    students = [-1] * 30
    for _ in range(28):
        tmp = int(input())
        students[tmp - 1] = 1

    for i in range(30):
        if students[i] == -1:
            print(i+1)


main()