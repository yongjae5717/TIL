import sys


def dfs(i, j):
    global flag, result
    if i == -1 or i == R:
        return
    if array[i][j] == 'x':
        return
    array[i][j] = 'x'
    if j == C - 1:
        flag = True
        result += 1
        return
    for k in range(3):
        dfs(i+di[k], j+dj[k])
        if flag:
            return


R, C = map(int, sys.stdin.readline().split())
array = [list(sys.stdin.readline().strip()) for _ in range(R)]
# print(array)
result = 0

di = [-1, 0, 1]
dj = [1, 1, 1]

for i in range(R):
    flag = False
    dfs(i, 0)

print(result)