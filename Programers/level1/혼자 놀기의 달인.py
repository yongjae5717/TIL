
cards = [8, 6, 3, 7, 2, 5, 1, 4]


def solution(cards):
    board = [[] for _ in range(len(cards))]

    for i in range(len(board)):
        temp = cards[i]
        for j in range(len(board)):
            board[i].append(temp)
            temp = cards[temp-1]
            if temp in board[i]:
                break
        board[i].sort()

    answer_list = list()
    for i in board:
        if i not in answer_list:
            answer_list.append(i)

    if len(answer_list) <= 1:
        return 0
    else:
        answer_list.sort (key=lambda x: len(x), reverse=True)
        return len(answer_list[0]) * len(answer_list[1])


print(solution(cards))