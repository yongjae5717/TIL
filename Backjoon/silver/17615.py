import sys
input = sys.stdin.readline


def main():
    n = int(input())
    ball = list(input().strip())

    if n == 1:
        return 0

    result_1 = 0
    # 왼쪽에 빨강색 공을 모으는 경우
    flag = False
    if ball[0] == 'R':
        flag = True
    for i in range(1, n):
        if ball[i] == 'R' and not flag:
            result_1 += 1
        elif ball[i] == 'B':
            flag = False

    # 왼쪽에 파란 공을 모으는 경우
    result_2 = 0
    flag = False
    if ball[0] == 'B':
        flag = True
    for i in range(1, n):
        if ball[i] == 'B' and not flag:
            result_2 += 1
        elif ball[i] == 'R':
            flag = False

    # 오른쪽에 빨강색 공을 모으는 경우
    ball = list(reversed(ball))
    result_3 = 0
    flag = False
    if ball[0] == 'R':
        flag = True
    for i in range(1, n):
        if ball[i] == 'R' and not flag:
            result_3 += 1
        elif ball[i] == 'B':
            flag = False

    # 오른쪽에 파란 공을 모으는 경우
    result_4 = 0
    flag = False
    if ball[0] == 'B':
        flag = True
    for i in range(1, n):
        if ball[i] == 'B' and not flag:
            result_4 += 1
        elif ball[i] == 'R':
            flag = False

    return min(result_1, result_2, result_3, result_4)


print(main())