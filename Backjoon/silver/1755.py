import sys
input = sys.stdin.readline


def main():
    m, n = map(int, input().split())
    dict_num = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
                5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    num = list()
    for i in range(m, n + 1):
        number = ""
        for c in str(i):
            number += dict_num[int(c)] + " "
        num.append([number, i])
    num.sort()

    count = 0
    result = ""
    for i in num:
        count += 1
        result += str(i[1]) + " "
        if count % 10 == 0:
            print(result.strip())
            result = ""
    print(result.strip())


main()