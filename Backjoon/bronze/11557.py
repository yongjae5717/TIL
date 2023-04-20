import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        school = list()
        for _ in range(n):
            name, quantity = input().split()
            school.append([name, int(quantity)])

        school.sort(key=lambda x: x[1], reverse=True)
        print(school[0][0])


main()