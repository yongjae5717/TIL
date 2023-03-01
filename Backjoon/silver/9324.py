import sys
input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        word = input().strip()
        dictionary = dict()
        dictionary[word[0]] = 1
        flag = True
        exception = False
        for c in range(1, len(word)):
            if exception:
                exception = False
                continue
            if word[c] not in dictionary:
                dictionary[word[c]] = 1
            else:
                dictionary[word[c]] += 1

            if dictionary[word[c]] % 3 == 0:
                if c == len(word) - 1:
                    flag = False
                    break
                if word[c] != word[c + 1]:
                    flag = False
                    break
                exception = True

        if flag:
            print("OK")
        else:
            print("FAKE")


main()