def solution(s):
    stack = list(str(s))
    dummy = list()
    temp = stack.pop()
    dummy.append(temp)

    while stack:
        temp = stack.pop()
        if len(dummy) == 0:
            dummy.append(temp)
        else:
            if temp == dummy[len(dummy)-1]:
                dummy.pop()
            else:
                dummy.append(temp)

    if dummy:
        return 0
    else:
        return 1