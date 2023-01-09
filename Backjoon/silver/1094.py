import sys
from collections import deque
input = sys.stdin.readline


def main():
    x = int(input())

    lst = deque([64])
    result = 64
    if result == x:
        return 1
    while x != result:
        temp = lst.pop()
        if result > x:
            result -= temp // 2
            lst.append(temp // 2)
        elif result < x:
            result += temp // 2
            lst.append(temp)
            lst.append(temp // 2)
        if result == x:
            return len(lst)


print(main())