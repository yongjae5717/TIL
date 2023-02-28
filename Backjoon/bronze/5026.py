import sys
input = sys.stdin.readline


def main():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if s.count("+") != 0:
            print(sum(map(int, s.split("+"))))
        elif s == "P=NP":
            print("skipped")


main()