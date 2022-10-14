import sys

N = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))

# +, -, *, /
operator = list(map(int, sys.stdin.readline().split()))

result_list = list()


def DFS(count, add, sub, mul, div, s):
    if add < 0 or sub < 0 or mul < 0 or div < 0:
        return

    if count == N:
        result_list.append(s)
        return

    DFS(count + 1, add - 1, sub, mul, div, s + array[count])
    DFS(count + 1, add, sub - 1, mul, div, s - array[count])
    DFS(count + 1, add, sub, mul - 1, div, s * array[count])
    DFS(count + 1, add, sub, mul, div - 1, int(s / array[count]))


DFS(1, operator[0], operator[1], operator[2], operator[3], array[0])
print(max(result_list))
print(min(result_list))