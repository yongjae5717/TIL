def solution(s, n):
    result = ''
    for i in s:
        idx = ord(i)
        if 65 <= idx <= 90:
            idx += n
            if idx >90:
                idx -= 26
        elif 97 <= idx <= 122:
            idx += n
            if idx > 122:
                idx -= 26
        result += chr(idx)
    return result


def solution2(s, n):
    result = ''
    for i in s:
        idx = ord (i)
        if 'a' <= i <= 'z':
            idx += n
            if chr(idx) > 'z':
                idx -= 26
        elif 'A' <= i <= 'Z':
            idx += n
            if chr(idx) > 'Z':
                idx -= 26
        result += chr(idx)
    return result