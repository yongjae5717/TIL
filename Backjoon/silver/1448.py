import sys
input = sys.stdin.readline


def main():
    n = int(input())
    straw = list(int(input()) for _ in range(n))
    straw.sort(reverse=True)
    res = -1
    for i in range(n - 2):
        tmp = straw[i:i+3]
        if is_triangle(tmp):
            res = max(res, sum(tmp))
    print(res)


def is_triangle(triangle):
    triangle.sort()
    a, b, c = triangle
    if c < b + a:
        return True
    else:
        return False


main()