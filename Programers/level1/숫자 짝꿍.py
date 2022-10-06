def solution(X, Y):
    xList = list(X.count(str(x)) for x in range(10))
    yList = list(Y.count(str(y)) for y in range(10))
    answer = ""
    for i in range(9, -1, -1):
        answer += str(i) * min(xList[i], yList[i])

    if answer == "":
        return "-1"
    elif answer[0] == "0" and answer[len(answer) - 1] == "0":
        return "0"
    else:
        return answer