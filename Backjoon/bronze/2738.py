def main():
    n, m = map(int, input().split())
    array_1 = list(list(map(int, input().split())) for _ in range(n))
    array_2 = list(list(map(int, input().split())) for _ in range(n))

    res = list([0] * m for _ in range(n))
    for i in range(n):
        for j in range(m):
            res[i][j] = array_1[i][j] + array_2[i][j]

    for r in res:
        print(*r)


main()