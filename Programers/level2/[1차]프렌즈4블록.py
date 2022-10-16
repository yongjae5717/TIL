def solution(m, n, board):
    board = list(list(i) for i in board)
    answer = 0
    while True:
        # for i in board:
        #     print(i)
        # print("\n")
        temp = list()
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] == "0":
                    continue
                if board[i][j] == board[i][j+1] and board[i][j] == board[i+1][j] and board[i][j] == board[i+1][j+1]:
                    temp.append((i, j))
                    temp.append((i, j+1))
                    temp.append((i+1, j))
                    temp.append((i+1, j+1))

        if len(temp) == 0:
            break

        answer += len(set(temp))
        for i in temp:
            board[i[0]][i[1]] = "0"

        for i in reversed(temp):
            column = i[1]
            afterRow = i[0]
            beforeRow = i[0] - 1
            while beforeRow >= 0:
                if board[afterRow][column] == "0" and board[beforeRow][column] != "0":
                    board[afterRow][column] = board[beforeRow][column]
                    board[beforeRow][column] = "0"
                    afterRow -= 1
                beforeRow -= 1
    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))