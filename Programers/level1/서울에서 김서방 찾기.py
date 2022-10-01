def solution(seoul):
    answer = 0
    for i in seoul:
        if i == "Kim":
            return "김서방은 " + str(answer) + "에 있다"
        answer += 1