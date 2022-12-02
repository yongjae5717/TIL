import math


def solution(n, stations, w):
    result = 0
    zero = list()
    for i in range(1, len(stations)):
        zero.append((stations[i]-w-1)-(stations[i-1]+w))

    zero.append(stations[0] - w - 1)
    zero.append(n - (stations[-1] + w))

    width = 2 * w + 1

    for i in zero:
        if i <= 0:
            continue
        result += math.ceil(i/width)

    return result


print(solution(11, [4, 11], 1))