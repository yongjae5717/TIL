def solution(babbling):
    dictionary = {"aya": 3, "ye": 2, "woo": 3, "ma": 2}

    answer = 0
    for b in babbling:
        temp = b
        check = True
        before = ""
        while temp:
            if temp[:3] in dictionary:
                if before == temp[:3]:
                    check = False
                    break
                before = temp[:3]
                temp = temp[3:]
            elif temp[:2] in dictionary:
                if before == temp[:2]:
                    check = False
                    break
                before = temp[:2]
                temp = temp[2:]
            else:
                check = False
                break
        if check:
            answer += 1

    return answer


print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))