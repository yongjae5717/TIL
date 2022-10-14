import sys


def dfs(x, y):
    global count, N, maps
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if maps[x][y] == 1:
        count += 1
        maps[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x + 1, y)
        return True
    return False


N = int(sys.stdin.readline())
maps = list()
for i in range(N):
    maps.append(list(map(int, sys.stdin.readline().strip())))
count, result = 0, 0
result_list = list()
for i in range(N):
    for j in range(N):
        if dfs(i, j) is True:
            result += 1
            result_list.append(count)
            count = 0

result_list.sort()
print(result)
for k in result_list:
    print(k)