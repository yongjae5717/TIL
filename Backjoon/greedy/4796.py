# 예제
# 입력 (L P V) (1 < L < P < V)
# 5 8 20
# 5 8 17
# 0 0 0


# 출력
# Case1: 14
# Case2: 11


import sys


def main():
    inp = ""
    inp_list = list()
    while inp != "0 0 0":
        inp = input()
        inp_list.append(inp.split())

    scalar, remain, L, P, V, result = 0, 0, 0, 0, 0, 0

    for i in range(len(inp_list) - 1):
        L = int(inp_list[i][0])
        P = int(inp_list[i][1])
        V = int(inp_list[i][2])
        # print(L, P, V)
        scalar = V // P
        remain = V % P
        if remain >= L:
            result = scalar * L + L
        else:
            result = scalar * L + remain
        print("Case " + str(i+1) + ": " + str(result))


main()