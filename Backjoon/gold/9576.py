import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        books = [0] * (n+1)
        lst = list(list(map(int, input().split())) for _ in range(m))
        lst.sort(key=lambda x: x[1])

        count = 0
        while lst:
            a, b = lst.pop(0)

            for i in range(a, b+1):
                if books[i] == 0:
                    count += 1
                    books[i] = 1
                    break
        print(count)


main()