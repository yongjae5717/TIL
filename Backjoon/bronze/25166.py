import sys
input = sys.stdin.readline


def main():
    s, m = map(int, input().split())
    if s < 1024:
        print("No thanks")
    else:
        ari = s - 1023
        cookie = m
        if ari & cookie == ari:
            print("Thanks")
        else:
            print("Impossible")


main()