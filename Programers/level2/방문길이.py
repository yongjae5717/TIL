def solution(dirs):
    # 초기 지점 x, y좌표
    x, y = 5, 5
    # 결과값
    count = 0
    # set을 이용한 중복제거
    settemp = set()

    # 문자 U,D,R,L당 x, y좌표 변경 (board반경내에서)
    for c in dirs:
        temp_x, temp_y = x, y
        if c == "U":
            y -= 1
        elif c == "D":
            y += 1
        elif c == "R":
            x += 1
        elif c == "L":
            x -= 1

        # board반경을 넘어가는 경우 예외처리
        if x > 10:
            x = 10
        if x < 0:
            x = 0
        if y > 10:
            y = 10
        if y < 0:
            y = 0

        # 반경을 넘어갔다면 동일한 값 (전 == 후)
        if temp_x == x and temp_y == y:
            continue

        # 동일한 값이 아니라면 이전값과 이후값을 set에 넣어준다. (tip, 전 -> 후 , 후 -> 전은 같은 길)
        elif (temp_x, temp_y, x, y) not in settemp:
            settemp.add((x, y, temp_x, temp_y))
            settemp.add((temp_x, temp_y, x, y))
            count += 1

    return count


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))