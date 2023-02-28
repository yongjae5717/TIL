import sys, re
input = sys.stdin.readline


def main():
    n = int(input())
    word = input().strip()
    find_number = re.findall("\d+", word)
    res = 0
    for num in find_number:
        res += int(num)
    print(res)


main()