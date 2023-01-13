import sys
input = sys.stdin.readline


def main():
    n = int(input())
    condo_row = list(input().strip() for _ in range(n))
    condo_row.append("X" * n)
    condo_col = list("" for _ in range(n+1))

    for i in range(n+1):
        condo_row[i] += 'X'
        for j in range(n+1):
            condo_col[i] += condo_row[j][i]
        condo_col[i] += 'X'

    col, row = 0, 0
    for condo in zip(condo_row, condo_col):
        r, c = condo
        r_count, c_count = 0, 0
        for x in r:
            if x == '.':
                r_count += 1
            elif x == 'X':
                if r_count >= 2:
                    row += 1
                r_count = 0

        for y in c:
            if y == '.':
                c_count += 1
            elif y == 'X':
                if c_count >= 2:
                    col += 1
                c_count = 0
    print(row, col)


main()