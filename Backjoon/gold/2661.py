import sys
input = sys.stdin.readline

s = list()


def solution(n, idx):
    global s
    # 연속된 숫자가 나오는지 확인
    for i in range(1, (idx//2) + 1):
        if s[-i:] == s[-2 * i:-i]:
            return
    # n의 길이가 나오면 종료
    if idx == n:
        for i in range(n):
            print(s[i], end='')
        return 0

    # 백트래킹
    for i in range(1, 4):
        s.append(i)
        if solution(n, idx + 1) == 0:
            return 0
        s.pop()


def main():
    n = int(input())
    solution(n, 0)


main()