import sys
input = sys.stdin.readline
k, l = map(int, input().split())


def solution(k, l):
    students = dict()
    for i in range(l):
        studentNumber = input().strip()
        students[studentNumber] = i

    studentsList = sorted(students.items(), key=lambda x: x[1])
    for i in range(min(len(studentsList), k)):
        print(studentsList[i][0])


solution(k, l)