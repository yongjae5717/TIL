import sys
input = sys.stdin.readline


def main():
    words = list(list(input().strip()) for _ in range(5))
    for i in range(5):
        tmp = 15 - len(words[i])
        for _ in range(tmp):
            words[i].append("|")
    res = ''
    for i in zip(words[0], words[1], words[2], words[3], words[4]):
        tmp = ''
        for c in i:
            tmp += c
        res += tmp
    res = res.replace("|", "")
    print(res)


main()