def solution(sizes):
    row, column = 0, 0
    for point in sizes:
        x, y = max(point), min(point)
        row = max(x, row)
        column = max(y, column)
    return row * column