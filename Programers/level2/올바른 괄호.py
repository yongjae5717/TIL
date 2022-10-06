def solution(s):
    stack = list(s)
    count = 0
    while stack:
        temp = stack.pop()
        if temp == ")":
            count += 1
        else:
            if count > 0:
                count -= 1
            else:
                return False
    if count == 0:
        return True
    else:
        return False