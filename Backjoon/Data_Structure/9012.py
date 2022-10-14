import sys
input = sys.stdin.readline

T = int(input())


def VPS(inp_str):
    result = 0

    for i in inp_str:
        if i == '(':
            result += 1
        elif i == ')':
            result -= 1

        if result < 0:
            break
    return result


for _ in range(T):
    inp_str = list(input().strip())

    ans = VPS(inp_str)
    if ans == 0:
        print("YES")
    else:
        print("NO")