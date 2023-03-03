import sys
input = sys.stdin.readline

digit = [
    "####.##.##.####",
    "..#..#..#..#..#",
    "###..#####..###",
    "###..####..####",
    "#.##.####..#..#",
    "####..###..####",
    "####..####.####",
    "###..#..#..#..#",
    "####.#####.####",
    "####.####..####"]

lst = list(list(input().strip()) for _ in range(5))


def match(x, k):
    for i in range(5):
        for j in range(3):
            if lst[i][x+j] == '#' and digit[k][i*3 + j] == '.':
                return False
    return True


def main():
    timer = [2, 9, 5, 9]
    for x in range(4):
        for k in range(timer[x]+1):
            if match(4*x, k):
                print(k, end="")
                break
        if x == 1:
            print(":", end="")


main()