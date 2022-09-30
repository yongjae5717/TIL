def solution(x):
    temp = 0
    for i in str(x):
        temp += int(i)
    if x % temp == 0:
        return True
    return False