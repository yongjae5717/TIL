import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lectures = list(list(map(int, input().split())) for _ in range(n))
    m = int(input())
    studies = list(list(map(int, input().split())) for _ in range(m))

    for i in range(m):
        count = n
        for lecture in lectures:
            for time in lecture[1:]:
                if time not in studies[i][1:]:
                    count -= 1
                    break
        print(count)


main()