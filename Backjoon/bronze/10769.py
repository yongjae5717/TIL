import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    up_count = s.count(':-)')
    down_count = s.count(':-(')
    if up_count > down_count:
        print("happy")
    elif down_count > up_count:
        print("sad")
    elif up_count == down_count and up_count != 0:
        print("unsure")
    else:
        print("none")


main()