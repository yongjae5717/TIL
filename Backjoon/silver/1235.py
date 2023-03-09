import sys
input = sys.stdin.readline


def main():
    n = int(input())
    student_id = list(input().strip() for _ in range(n))
    count = 1
    while True:
        tmp = set()
        for s in student_id:
            tmp.add(s[len(s)-count:])
        if len(tmp) == n:
            break
        count += 1
    print(count)


main()