# N: 끊어진 기타줄의 개수
# M: 기타줄 브랜드
# 6개 패키지 가격(P), 낱개로 살 때(S)의 가격

import sys


def main():
    N, M = map(int, sys.stdin.readline().split())
    P_list = list()
    S_list = list()
    for _ in range(M):
        P, S = map(int, sys.stdin.readline().split())
        P_list.append(P)
        S_list.append(S)

    P_list.sort()
    S_list.sort()
    # print(P_list[0], S_list[0])

    result = 0
    if P_list[0] > S_list[0] * 6:
        result = N * S_list[0]
    elif N % 6 == 0:
        result = (N // 6) * P_list[0]
    elif (N - (N // 6) * 6) * S_list[0] > P_list[0]:
        result = ((N // 6) + 1) * P_list[0]
    else:
        result = (N // 6) * P_list[0] + (N - (N // 6) * 6) * S_list[0]
    print(result)


main()