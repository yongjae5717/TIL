import sys, re
input = sys.stdin.readline


def main():
    res = ""
    count = 0
    while True:
        tmp = input().strip()
        a = re.findall("[a-zA-Z-]+", tmp)
        a.sort(key=lambda x: len(x), reverse=True)
        if a:
            len_a = len(a[0])
            if len_a > count:
                count = len_a
                res = a[0]
        if a.count("E-N-D"):
            break
    print(res.lower())


main()