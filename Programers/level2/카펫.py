def solution(brown, yellow):
    S = brown + yellow
    for i in range(S-1, -1, -1):
        if S % i != 0:
            continue

        height = S // i
        y = (i - 2) * (height - 2)
        b = S - y

        if yellow == y and brown == b:
            return [i, height]