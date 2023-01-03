import sys
input = sys.stdin.readline


def main():
    n = int(input())
    s = list(map(int, input().split()))
    s.sort()

    result_num = list()
    for i in range(n):
        result_num.append(s[i] + s[2*n-1-i])

    print(min(result_num))


main()