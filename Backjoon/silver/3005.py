import sys
input = sys.stdin.readline


def main():
    r, c = map(int, input().split())
    words = [input().strip() for _ in range(r)]
    col = list()
    for i in range(c):
        tmp = ""
        for j in range(r):
            tmp += words[j][i]
        col.append(tmp)
    words += col

    res = list()
    for word in words:
        tmp = ""
        for c in word:
            if c == "#":
                if len(tmp) >= 2:
                    res.append(tmp)
                tmp = ""
            else:
                tmp += c
        if len(tmp) >= 2:
            res.append(tmp)
    res.sort()
    print(res[0])


main()