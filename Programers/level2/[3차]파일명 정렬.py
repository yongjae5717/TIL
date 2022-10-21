def solution(files):
    answer = list()
    for f in files:
        """
        lst[0]: HEAD
        lst[1]: NUMBER
        lst[2]: TAIL
        """

        count = -1
        flag = False
        lst = ["", "", ""]
        for c in f:
            # 만약 처음에 들어왔을 경우 카운트를 0부터 시작하도록 만들어 줌 (HEAD의 경우)
            if c.isdigit() is False and flag is False:
                flag = True
                count += 1
            # NUMBER의 경우 flag를 이용하여 예외 처리를 해준다.
            elif flag and c.isdigit():
                flag = False
                count += 1

            # 만약 또 숫자가 들어와서 index out of range가 될 경우를 방지해준다.
            if count > 2:
                count = 2

            # HEAD, NUMBER, TAIL을 count를 이용하여 Index로 사용한다.
            lst[count] += c
        answer.append(lst)

    # HEAD의 경우 사전순으로 정렬(대소문자 구분 x, 만약 같다면 들어온 순서대로), 그리고 NUMBER의 경우 작은 숫자 순으로 오름차순 정렬한다.
    answer.sort(key=lambda x: (x[0].lower(), int(x[1])))

    # 결과를 HEAD, NUMBER, TAIL이 아닌 String의 형태로 반환한다.
    result = []
    for a in answer:
        temp = "".join(a)
        result.append(temp)
    return result


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["foo9.txt", "foo010bar020.zip", "F-15"]))