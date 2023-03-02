import sys
input = sys.stdin.readline


def main():
    n = int(input())
    lst = list(list(map(int, input().split())) for _ in range(n))
    lst.sort(key=lambda x: x[2], reverse=True)

    res = list()
    dictionary = dict()
    count = 0
    for i in lst:
        nation, student_id, score = i
        if nation not in dictionary:
            dictionary[nation] = 1
        else:
            dictionary[nation] += 1
        if dictionary[nation] <= 2:
            res.append([nation, student_id])
            count += 1
        if count == 3:
            break
    for r in res:
        print(*r)

main()