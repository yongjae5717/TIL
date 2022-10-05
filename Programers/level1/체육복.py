def solution(n, lost, reserve):
    # 초기값 셋팅 (0, n+1인덱스는 좌 우 비교를 위함)
    students = [1] * (n + 2)

    # 체육복을 도난당하면 0으로 변경
    for i in lost:
        students[i] -= 1

    # 여벌의 체육복을 가져왔으면 +1
    for i in reserve:
        students[i] += 1

    for i in range(1, n + 1):
        # 현재 학생이 체육복을 도난 당했을 때, 앞자리학생이 여분을 가져온 경우
        if students[i] == 0 and students[i-1] == 2:
            students[i-1] -= 1
            students[i] += 1
        # 현재 학생이 체육복을 도난 당했을 때, 뒷자리학생이 여분을 가져온 경우
        elif students[i] == 0 and students[i+1] == 2:
            students[i+1] -= 1
            students[i] += 1
    print(students)
    # -2를 해준 이유? students의 0번째 인덱스와 n+1번째 인덱스는 앞뒤에 사람이 없는 자리의 경우를 대비함
    return students.count(1) + students.count(2) - 2