def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isdigit():
                continue
            else:
                return False
        return True
    else:
        return False