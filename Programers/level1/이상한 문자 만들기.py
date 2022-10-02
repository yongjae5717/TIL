def solution(s):
    result = ''
    temp = ''
    count = 1
    for i in s:
        if temp == ' ':
            count = 1

        if count % 2 == 0:
            result += i.lower ()
        else:
            result += i.upper ()

        temp = i
        count += 1
    return result