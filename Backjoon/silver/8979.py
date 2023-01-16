import sys
input = sys.stdin.readline


def main():
    global index
    n, k = map(int, input().split())
    s = list(list(map(int, input().split())) for _ in range(n))
    s.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))

    for i in range(n):
        if s[i][0] == k:
            index = i
    for i in range(n):
        if s[index][1:] == s[i][1:]:
            print(i + 1)
            break


main()


''' 20점짜리 답변

import sys
input = sys.stdin.readline


def compare(num1, num2, lst, k):
    count1, gold1, silver1, bronze1 = lst[num1][1]
    count2, gold2, silver2, bronze2 = lst[num2][1]
    if len(lst) == 2:
        for i in lst:
            result, temp = i
            if temp[0] == k:
                return result + 1

    elif gold1 == gold2 and silver1 == silver2 and bronze1 == bronze2:
        if num2 == 0:
            return 1
        return compare(num1, num2-1, lst, k)
    else:
        return lst[num2][0] + 2


def main():
    n, k = map(int, input().split())
    if n == 1:
        print(1)
        exit(0)

    nation = list(list(map(int, input().split())) for _ in range(n))
    nation.sort(reverse=True, key=lambda x: (x[1], x[2], x[3]))

    temp = list(enumerate(nation))

    for i in range(n):
        count, lst = temp[i]
        if lst[0] == k:
            print(compare(count, count - 1, temp, k))
            break


main()
'''
