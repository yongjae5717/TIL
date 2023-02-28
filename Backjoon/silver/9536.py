import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        s = list(input().split())
        res = list()
        animals = list()
        while True:
            tmp = input().strip()
            if tmp == "what does the fox say?":
                break
            tmp_list = tmp.split()
            animals.append(tmp_list[2])

        for sound in s:
            if sound not in animals:
                res.append(sound)
        print(*res)


main()