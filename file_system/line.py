import sys
input = sys.stdin.readline


def main():
    filename = sys.argv[1]

    f = open(filename, "r")
    count = 0
    for i in f:
        print(f"{count}" + i)
        count += 1


if __name__ == "__main__":
    main()