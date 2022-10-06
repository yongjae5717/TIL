def solution(s):
    step_count, zero_count = 0, 0

    while len (s) != 1:
        lst = list (s)
        step_count += 1
        zero_count += lst.count ("0")
        temp = lst.count ("1")
        s = ""
        while temp >= 1:
            s += str (temp % 2)
            temp = int((temp - temp % 2) / 2)

    return [step_count, zero_count]