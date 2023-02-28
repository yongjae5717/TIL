import sys, re
input = sys.stdin.readline


def main():
    n = int(input())
    res = list()
    for _ in range(n):
        line_num = re.findall("\d+", input().strip())
        for num in line_num:
            res.append(int(num))
    res.sort()
    print(* res)


main()