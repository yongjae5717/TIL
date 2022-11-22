def solution(arr):
    answer = [0, 0]
    n = len(arr)
    func(0, 0, n, arr, answer)
    return answer


def func(x, y, n, arr, answer):
    temp = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != temp:
                func(x, y, n//2, arr, answer)
                func(x, y + n//2, n//2, arr, answer)
                func(x + n//2, y, n//2, arr, answer)
                func(x + n//2, y + n//2, n//2, arr, answer)
                return
    answer[temp] += 1


print(solution([[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]))
print(solution([[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]))