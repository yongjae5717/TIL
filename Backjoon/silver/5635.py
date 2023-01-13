import sys
input = sys.stdin.readline


def main():
    n = int(input())
    ddmmyyyy = list()
    for _ in range(n):
        name, day, month, year = input().split()
        if len(day) == 1:
            day = "0" + day
        if len(month) == 1:
            month = "0" + month
        temp = year + month + day
        ddmmyyyy.append((name, int(temp)))

    ddmmyyyy.sort(key=lambda x: x[1])
    print (ddmmyyyy[-1][0])
    print(ddmmyyyy[0][0])


main()