import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    while s != "*":
        flag = False
        sentence = s.split()
        tmp = sentence[0][0].lower()
        for word in sentence:
            if word[0].lower() != tmp:
                flag = True
                break
        if flag:
            print("N")
        else:
            print("Y")
        s = input().strip()


main()