import sys
input = sys.stdin.readline


def main():
    studies = list(list(map(str, input().split())) for _ in range(20))
    total_credit, total_score = 0, 0
    score = {'A+':4.5, 'A0':4, 'B+':3.5, 'B0':3, 'C+':2.5, 'C0':2, 'D+':1.5, 'D0':1, 'F':0}

    for s in studies:
        name, credit, grade = s
        if grade == 'P':
            continue
        total_credit += int(credit[0])
        total_score += int(credit[0]) * score[grade]

    print(total_score / total_credit)


main()