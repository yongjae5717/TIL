import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        dictionary = dict()
        n = int(input())
        for _ in range(n):
            name, type = input().split()
            if type not in dictionary:
                dictionary[type] = []
                dictionary[type].append(name)
            else:
                dictionary[type].append(name)
        count = 1
        lst = list(dictionary.items())
        for i in lst:
            count *= len(i[1]) + 1
        print(count - 1)


main()