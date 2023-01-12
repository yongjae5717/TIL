import sys
input = sys.stdin.readline


def main():
    dictionary = dict()
    s = input().strip()
    length = 0
    while length != len(s):
        length += 1
        for i in range(len(s)):
            if s[i:i+length] not in dictionary:
                dictionary[s[i:i+length]] = 1
    return len(dictionary)


print(main())