import sys
input = sys.stdin.readline


def main():
    n = int(input())
    file_size = list(map(int, input().split()))
    cluster_size = int(input())
    disk = 0
    for f in file_size:
        if f > 0:
            disk += cluster_size * ((f-1) // cluster_size + 1)
    print(disk)


main()