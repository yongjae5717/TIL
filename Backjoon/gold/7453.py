import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    # print(lst)
    ab, cd = list(), list()

    for i in range(n):
        for j in range(n):
            ab.append(lst[i][0] + lst[j][1])
            cd.append(lst[i][2] + lst[j][3])

    ab.sort()
    cd.sort()
    # print(ab, cd)

    result = 0
    i, j = 0, len(cd)-1
    while i < len(ab) and j >= 0:
        if ab[i] + cd[j] == 0:
            # 출처: https://www.acmicpc.net/source/26772324
            # ab나 cd가 여러개인 경우를 생각해야함.
            nexti, nextj = i + 1, j - 1
            # ab가 같은게 여러개인경우
            while nexti < len(ab) and ab[i] == ab[nexti]:
                nexti += 1
            # cd가 같은게 여러개인경우
            while nextj >= 0 and cd[j] == cd[nextj]:
                nextj -= 1

            result += (nexti - i) * (j - nextj)
            i, j = nexti, nextj
        elif ab[i] + cd[j] > 0:
            j -= 1
        else:
            i += 1
    print(result)


main()