import sys


def R_cal():
    global array, len_row

    for row in range(len(array)):
        cal = list()
        cnt = [0] * 100
        # counter 이용
        for i in array[row]:
            if i == 0: continue
            cnt[i-1] += 1
        # 수, 카운트를 튜플로 묶음
        for j in range(100):
            if cnt[j] == 0: continue
            cal.append((j + 1, cnt[j]))
        # 수가 작은 순서, 같을 경우 작은 것 먼저
        cal.sort(key=lambda x: (x[1], x[0]))

        temp = list()
        for k in cal:
            temp.append(k[0])
            temp.append(k[1])

        # 행 길이 맞추기 + array 변경된 값으로 저장
        len_row = max(len_row, len(temp))
        array[row] = temp

    # 남은 공간 0으로 저장
    for row in range(len(array)):
        n = len_row - len(array[row])
        array[row] += [0] * n


def C_cal():
    global array, len_column
    for col in range(len_row):
        cal = list()
        cnt = [0] * 100
        temp_len = len_column

        # Counter 이용
        for i in range(len_column):
            if array[i][col] == 0: continue
            cnt[array[i][col] - 1] += 1
        # cal (수, 수의 개수) 저장
        for j in range(100):
            if cnt[j] == 0: continue
            cal.append((j+1, cnt[j]))

        cal.sort(key=lambda x: (x[1], x[0]))

        temp = list()
        for k in cal:
            temp.append(k[0])
            temp.append(k[1])

        len_column = max(len_column, len(temp))

        # 남은부분 0으로 채우기
        for l in range(len_column):
            if l >= temp_len:
                array.append([0 for _ in range(len_row)])
                temp_len += 1
            if l >= len(temp):
                array[l][col] = 0
                continue

            array[l][col] = temp[l]


# row, column, result: array[r][c] = k를 찾아라
r, c, k = map(int, sys.stdin.readline().split())

# array 초기화 3x3행렬
array = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

len_row, len_column = 3, 3
# 100초 조건
for t in range(101):
    # array[r][c]가 k와 같으면 출력
    if r <= len_column and c <= len_row and array[r-1][c-1] == k:
        print(t)
        break

    if len_row <= len_column:
        # R연산
        R_cal()
    else:
        # C연산
        C_cal()
    if t == 100:
        print(-1)
        break