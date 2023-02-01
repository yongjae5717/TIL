# 리틀앤디언
def to_le(bytes):
    result = ""
    for b in bytes[::-1]:
        temp = str(hex(b)[2:])
        if len(temp) == 1:
            temp = "0" + temp
        result += temp
    return result


# 빅앤디언
def to_be(bytes):
    result = ""
    for b in bytes:
        temp = str(hex(b)[2:])
        if len(temp) == 1:
            temp = "0" + temp
        result += temp
    return result
