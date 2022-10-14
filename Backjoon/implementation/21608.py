import sys

input = sys.stdin.readline

n = int(input())
student_list = list([0] * n for _ in range(n))
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
students = list()

for _ in range(n ** 2):
    # index 0: 학생의 번호, 나머지: 좋아하는 학생의 번호
    student = list(map(int, input().split()))

    # 전체 학생들 리스트 생성하기
    students.append(student)

    # 우선순위가 높은 것 부터 표현하는 리스트 생성
    temp = list()
    for i in range(n):
        for j in range(n):
            if student_list[i][j] == 0:
                like = 0
                n_like = 0
                # 상하 좌우 비교하기
                for k in range(len(d)):
                    dx = i + d[k][0]
                    dy = j + d[k][1]
                    if (0 <= dx < n) and (0 <= dy < n):
                        # 좋아하는 학생이 있는 경우
                        if student_list[dx][dy] in student[1:]:
                            like += 1
                        # 비어있는 경우
                        if student_list[dx][dy] == 0:
                            n_like += 1
                temp.append([like, n_like, i, j])

    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    x, y = temp[0][2], temp[0][3]
    # n * n 행렬에 학생의 번호 넣어주기
    student_list[x][y] = student[0]

# for i in student_list:
#     print(i)

# 결과값 출력
result_point = 0
# 학생의 번호순서대로 정렬
students.sort()
for i in range(n):
    for j in range(n):
        count = 0
        for k in range(len(d)):
            dx = i + d[k][0]
            dy = j + d[k][1]
            if 0 <= dx < n and 0 <= dy < n:
                if student_list[dx][dy] in students[student_list[i][j] - 1]:
                    count += 1
        # 좋아하는 사람이 한명도 없을 때 제외한 경우에만 점수 카운트
        # 이유: ** (0) 이라면 1이기 때문이다.
        if count != 0:
            result_point += 10 ** (count -1)

print(result_point)