def solution(s, skip, index):
    skip_ord = list(ord(c) for c in skip)
    res = list()
    for c in s:
        ord_c = ord(c)
        temp = index
        while temp != 0:
            ord_c += 1
            if ord_c not in skip_ord:
                temp -= 1
            if ord_c > ord('z'):
                temp_c = ord('a')
                while temp_c in skip_ord:
                    temp_c += 1
                ord_c = temp_c

        res.append(chr(ord_c))

    return "".join(res)


print(solution("aukks", "wbqd", 5))
print(solution("zzzzz", "a", 1))