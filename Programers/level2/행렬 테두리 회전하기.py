def solution(rows, columns, queries):
    answer = []
    table = list(list(i for i in range(1 + j * columns, columns * (j + 1) + 1)) for j in range(rows))

    for query in queries:
        x1, x2, y1, y2 = [x - 1 for x in query]
        tmp = table[x1][x2]
        res = tmp

        # left
        for i in range (x1 + 1, y1 + 1):
            table[i - 1][x2] = table[i][x2]
            res = min(res, table[i][x2])
        # bottom
        for i in range (x2 + 1, y2 + 1):
            table[y1][i - 1] = table[y1][i]
            res = min (res, table[y1][i])
        # right
        for i in range (y1 - 1, x1 - 1, -1):
            table[i + 1][y2] = table[i][y2]
            res = min (res, table[i][y2])
        # top
        for i in range (y2 - 1, x2 - 1, -1):
            table[x1][i + 1] = table[x1][i]
            res = min (res, table[x1][i])
        table[x1][x2 + 1] = tmp

        answer.append(res)
    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))
print(solution(100, 97, [[1,1,100,97]]))