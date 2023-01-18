import sys
from itertools import combinations
input = sys.stdin.readline


def main():
    s = input().strip()
    index = list(i for i in range(1, len(s)))
    arr = list()
    for combination in combinations(index, 2):
        p1, p2 = combination
        word1 = s[:p1]
        word2 = s[p1:p2]
        word3 = s[p2:]
        arr.append((word1[::-1] + word2[::-1] + word3[::-1]))

    arr.sort()
    print(arr[0])


main()