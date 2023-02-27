import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    if s[:2] == '0x':
        return int(s, 16)
    elif s[0] == '0' and len(s) != 1:
        return int(s, 8)
    else:
        return int(s)


print(main())