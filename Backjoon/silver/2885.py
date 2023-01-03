import sys
input = sys.stdin.readline


def main():
    k = int(input())
    count = 0
    size = 1
    while True:
        if size < k:
            count += 1
            size = 2 ** count
        else:
            break

    temp = size
    cut = 0
    while k > 0:
        if k >= temp:
            k -= temp
        else:
            temp //= 2
            cut += 1
    print(size, cut)


main()