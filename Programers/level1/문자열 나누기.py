def solution(s):
    result = 0

    temp = s[0]
    count1, count2 = 1, 0
    if len(s) == 1:
        return 1
    for i in range(1, len(s)):
        if count1 == 0:
            count1 += 1
            temp = s[i]
            if i == len(s) - 1 and count1 != 0:
                result += 1
            continue

        if s[i] == temp:
            count1 += 1
        else:
            count2 += 1

        if count1 == count2:
            result += 1
            count1, count2 = 0, 0

        if i == len(s) - 1 and count1 != 0:
            result += 1

    return result


print(solution("a"))
print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
