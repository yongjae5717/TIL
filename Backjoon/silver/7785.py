import sys
input = sys.stdin.readline


def main():
    n = int(input())
    log = set()
    for _ in range(n):
        name, type = map(str, input().split())
        if type == "enter":
            log.add(name)
        elif type == "leave":
            log.discard(name)
    res = list(log)
    res.sort(reverse=True)

    for l in res:
        print(l)


main()