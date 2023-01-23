import sys
input = sys.stdin.readline


def main():
    n, k = map(int, input().split())
    students = list(map(int, input().split()))
    students.sort()
    result = list()
    for i in range(1, n):
        result.append(students[i] - students[i-1])

    result.sort()
    # print (result)
    print(sum(result[::-1][k-1:]))


main()