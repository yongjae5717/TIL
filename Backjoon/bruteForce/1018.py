import sys

N, M = map(int, sys.stdin.readline().split())

array = [list(sys.stdin.readline().strip()) for _ in range(N)]
# print(array)
result_list = list()
for i in range(0, N - 7):
    for j in range(0, M - 7):
        first = array[i][j]
        last = array[i+7][j+7]
        count = -1
        result1 = 0
        result2 = 0
        # print(i, j)
        # if first == "B":
        for column in range(8):
            count += 1
            for row in range(8):
                if count % 2 == 1 and array[i + column][j + row] == "B":
                    result1 += 1
                elif count % 2 == 0 and array[i + column][j + row] == "W":
                    result1 += 1

                if count % 2 == 1 and array[i+column][j+row] == "W":
                    result2 += 1
                elif count % 2 == 0 and array[i+column][j+row] == "B":
                    result2 += 1
                count += 1
        result_list.append(64 - result1)
        result_list.append(64 - result2)

print(min(result_list))