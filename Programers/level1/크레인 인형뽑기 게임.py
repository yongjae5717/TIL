def solution(board, moves):
    N = len(board)
    result = list([0])
    answer = 0

    # moves의 원소를 for루프를 이용
    for i in moves:
        for j in range(N):
            # 만약 원소가 0이 아니라면 인형이 있는 것이다.
            if board[j][i-1] != 0:
                # 인형이 있는 것 중에서 이미 전에 뽑았으면 2개가 바구니에 연속해서 쌓이게 되기때문에 2개가 사라진다.
                if board[j][i-1] == result[len(result)-1]:
                    result.pop()
                    answer += 2
                # 이미 전에 뽑았지 않았다면 바구니에 추가한다
                else:
                    result.append(board[j][i-1])
                # 인형을 뽑았기때문에 인형을 없애준다.
                board[j][i-1] = 0
                break
    return answer