def solution(numbers, hand):
    answer = ''

    # 휴대폰 키패드 설정
    keyPad = [[1, 4, 7, "*"], [2, 5, 8, 0], [3, 6, 9, "#"]]

    leftIndex = [0, 4]  # "*"에서 시작
    rightIndex = [2, 4]  # "#"에서 시작

    # 0 ~ 9까지 y축을 value로 넣는다.
    keyIndex = [4, 1, 1, 1, 2, 2, 2, 3, 3, 3]

    for n in numbers:
        # 키패드의 왼쪽의 경우
        if n in keyPad[0]:
            answer += "L"
            leftIndex = [0, keyIndex[n]]
        # 키패드의 오른쪽의 경우
        elif n in keyPad[2]:
            answer += "R"
            rightIndex = [2, keyIndex[n]]
        # 키패드 중앙의 경우
        elif n in keyPad[1]:
            # 왼쪽 엄지손가락과 눌러야할 키패드의 길이
            left_distance = distance(leftIndex[0], leftIndex[1], 1, keyIndex[n])
            # 오른쪽 엄지손가락과 눌러야할 키패드의 길이
            right_distance = distance(rightIndex[0], rightIndex[1], 1, keyIndex[n])

            # 왼쪽이 가까운 경우
            if left_distance < right_distance:
                answer += "L"
                leftIndex = [1, keyIndex[n]]
            # 오른쪽이 가까운 경우
            elif left_distance > right_distance:
                answer += "R"
                rightIndex = [1, keyIndex[n]]
            # 왼쪽과 오른쪽의 길이가 동일한 경우 (hand에 따라 결정)
            else:
                if hand == "right":
                    answer += "R"
                    rightIndex = [1, keyIndex[n]]
                elif hand == "left":
                    answer += "L"
                    leftIndex = [1, keyIndex[n]]

    return answer


def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)