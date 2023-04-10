import sys
input = sys.stdin.readline


def main():
    n, m = 9, 9

    board = list(list(map(int, input().split())) for _ in range(m))

    count = 0
    max_value = [0, [0, 0]]
    for i in board:
        max_i = max(i)
        max_index = i.index(max_i)
        if max_value[0] <= max_i:
            max_value[0] = max_i
            max_value[1] = [count + 1, max_index + 1]
        count += 1

    res_value, row_col = max_value
    print(res_value)
    print(*row_col)


main()