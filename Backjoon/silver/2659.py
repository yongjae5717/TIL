import sys
input = sys.stdin.readline


def get_clock_num(n):
    inp = n
    lst = list()
    lst.append(int(inp))
    for _ in range(3):
        head, tail = inp[0], inp[1:]
        inp = tail + head
        lst.append(int(inp))

    res = sorted(lst)[0]
    return res


def main():
    tmp = input().strip().replace(" ", "")
    res = get_clock_num(tmp)

    n_clock = 1
    for i in range(1111, res):
        if '0' not in str(i) and i == get_clock_num(str(i)):
            n_clock += 1
    print(n_clock)


main()