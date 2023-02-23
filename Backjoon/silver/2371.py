import sys
input = sys.stdin.readline


def main():
    n = int(input())
    files = list()
    for i in range(n):
        files.append(list(input().split()))
    files.sort(key=lambda x: len(x))
    for i in range(1, len(files[-1])+1):
        temp = list()
        for file in files:
            # print(file[:i])
            if file[:i] not in temp:
                temp.append(file[:i])
            else:
                break
        # print(temp)
        if len(temp) == n:
            return i


print(main())