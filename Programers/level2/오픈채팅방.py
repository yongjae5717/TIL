def solution(record):
    dictionary = dict()
    answer = []

    # uid의 닉네임 (최신순)
    for i in record:
        temp = i.split()
        if len(temp) == 3:
            dictionary[temp[1]] = temp[2]

    # 입장, 퇴장, 변경
    for i in record:
        temp = i.split()
        if temp[0] == "Enter":
            answer.append(dictionary[temp[1]] + "님이 들어왔습니다.")
        elif temp[0] == "Leave":
            answer.append(dictionary[temp[1]] + "님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))