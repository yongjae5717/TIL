def main():
    s = input()
    n = int(input())
    res = 0
    for _ in range(n):
        ring = input()
        if s in ring * 2:
            res += 1
    print(res)


if __name__ == '__main__':
    main()