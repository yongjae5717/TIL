import sys


def main():
    inp1, inp2 = map(str, sys.stdin.readline().split())
    number1 = [0, 0] # max, min
    number2 = [0, 0] # max, min
    for i in inp1:
        if i == "5":
            i = "6"
        number1[0] = number1[0] * 10 + int(i)

    for i in inp1:
        if i == "6":
            i = "5"
        number1[1] = number1[1] * 10 + int(i)

    for i in inp2:
        if i == "5":
            i = "6"
        number2[0] = number2[0] * 10 + int(i)

    for i in inp2:
        if i == "6":
            i = "5"
        number2[1] = number2[1] * 10 + int(i)

    print(min(number1) + min(number2), max(number1) + max(number2))
    # print(number1, number2)


main()