import sys, math
input = sys.stdin.readline

n = int(input())  # 시험장
a = list(map(int, input().split()))  # 응시자 수
b, c = map(int, input().split())  # 총 감독관 감시자, 부 감독관 감시자


def solution(n_class, student, supervisor1, supervisor2):
    result = n_class
    for per_student in student:
        per_student -= supervisor1
        per_class_by_supervisor2 = math.ceil(per_student / supervisor2)
        if per_class_by_supervisor2 >= 0:
            result += per_class_by_supervisor2
    return result



print(solution(n, a, b, c))