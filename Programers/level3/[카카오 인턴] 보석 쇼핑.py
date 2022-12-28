def solution(gems):
    answer1, answer2 = 0, len(gems) - 1

    # 보석의 종류 갯수
    length = len(set(gems))

    # 시작점, 끝점
    start, end = 0, 0

    dictionary = dict()
    dictionary[gems[0]] = 1

    while start < len(gems) and end < len(gems):
        if len(dictionary) < length:
            end += 1
            if end == len(gems):
                break
            dictionary[gems[end]] = dictionary.get(gems[end], 0) + 1
        else:
            # 시작 끝 길이가 더 짧으면 변경
            if end - start + 1 < answer2 - answer1 + 1:
                answer1, answer2 = start, end

            if dictionary[gems[start]] == 1:
                del dictionary[gems[start]]
            else:
                dictionary[gems[start]] -= 1
            start += 1
    return [answer1 + 1, answer2 + 1]


lst = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(lst))