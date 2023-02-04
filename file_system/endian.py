# 리틀앤디언
def to_le(byte_array):
    result = ""
    for b in byte_array[::-1]:
        temp = str(hex(b)[2:])
        if len(temp) == 1:
            temp = "0" + temp
        result += temp
    return result


# 빅앤디언
def to_be(byte_array):
    result = ""
    for b in byte_array:
        temp = str(hex(b)[2:])
        if len(temp) == 1:
            temp = "0" + temp
        result += temp
    return result
