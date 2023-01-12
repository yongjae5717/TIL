import sys
input = sys.stdin.readline


def main():
    n = int(input())
    m = int(input())
    s = input().strip()

    position, count, result = 0, 0, 0

    while position < m - 1:
        if s[position:position+3] == 'IOI':
            count += 1
            position += 2
            if count == n:
                result += 1
                count -= 1
        else:
            position += 1
            count = 0

    return result


print(main())