import sys
input = sys.stdin.readline


def main():
    n = int(input())
    dictionary = dict()
    for _ in range(n):
        file_name, extension = input().strip().split('.')
        if extension not in dictionary:
            dictionary[extension] = 1
        else:
            dictionary[extension] += 1
    res = sorted(list(dictionary.items()))
    for r in res:
        print(*r)


main()