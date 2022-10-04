def solution(dartResult):
    lst = list ()
    temp = ""
    # [숫자], [S, D, T], [*, #] 구분하여 list 생성하기
    for i in dartResult:
        if i.isdigit ():
            temp += i
        else:
            if temp:
                lst.append (temp)
            temp = ""
            lst.append (i)

    # 다트를 3번 던지는 경우의 수를 num으로 정의
    num = [0] * 3
    count = -1

    for i in lst:
        if i.isdigit ():
            count += 1
            num[count] = int (i)
        # S, D, T일 경우 1,2,3제곱 한 수를 경우의 수에 넣기
        elif i == "S":
            num[count] = num[count] ** 1
        elif i == "D":
            num[count] = num[count] ** 2
        elif i == "T":
            num[count] = num[count] ** 3
        # 스타상
        elif i == "*":
            # 처음으로 던질때는 첫번째 다트만 곱하기 2
            if count == 0:
                num[count] *= 2
            # 처음이 아니라면 이전 다트 점수와 같이 곱하기 2
            else:
                num[count] *= 2
                num[count - 1] *= 2
        # 아차상은 현재 점수 곱하기 -1
        elif i == "#":
            num[count] *= -1
    # 다트 점수를 모두 더하면 최종점수가 나옴
    return sum (num)