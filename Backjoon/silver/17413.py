import sys
input = sys.stdin.readline


def main():
    s = input().strip()
    flag = False
    word = ""
    answer = ""

    for c in s:
        if not flag:
            if c == "<":
                flag = True
                word += c
            elif c == " ":
                word += c
                answer += word
                word = ""
            else:
                word = c + word

        else:
            word += c
            if c == ">":
                flag = False
                answer += word
                word = ""

    print(answer + word)


main()