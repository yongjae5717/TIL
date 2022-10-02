def solution(n, arr1, arr2):
    answer = []
    wall = '#'
    blank = ' '
    board1 = list ([0] * n for _ in range (n))
    board2 = list ([0] * n for _ in range (n))

    for i in range (len (arr1)):
        count1 = n - 1
        while arr1[i] >= 1:
            board1[i][count1] = int (arr1[i] % 2)
            arr1[i] = (arr1[i] - arr1[i] % 2) / 2
            count1 -= 1

    for i in range (len (arr2)):
        count2 = n - 1
        while arr2[i] >= 1:
            board2[i][count2] = int (arr2[i] % 2)
            arr2[i] = (arr2[i] - arr2[i] % 2) / 2
            count2 -= 1

    for i in range (n):
        temp = ''
        for j in range (n):
            if board1[i][j] == 0 and board2[i][j] == 0:
                temp += blank
            else:
                temp += wall
        answer.append (temp)

    return answer