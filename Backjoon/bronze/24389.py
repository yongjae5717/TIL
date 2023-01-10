import sys
input = sys.stdin.readline


def main():
    n = int(input())
    origin = bin(n)[2:]
    length = len(origin)
    origin = "0" * (32 - length) + origin
    # print(origin)

    origin = origin.replace("0", "x").replace("1", "y")
    origin = origin.replace("x", "1").replace("y", "0")
    changed_num = int(origin, 2) + 1
    changed_num = bin(changed_num)[2:]
    # print(changed_num)

    count = 0
    for i in range(32):
        if origin[i] == changed_num[i]:
            count += 1
    return count

print(main())