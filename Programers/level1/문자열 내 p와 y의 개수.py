def solution(s):
    countP, countY = 0, 0
    for i in s:
        if i == 'P' or i == 'p':
            countP += 1
        elif i == 'Y' or i == 'y':
            countY += 1
    if countP == countY:
        return True
    return False