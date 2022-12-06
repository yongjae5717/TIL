def solution(k, d):
    result = 0
    for i in range(0, d+1, k):
        dis = distance(d, i)
        result += dis // k + 1
    return result


def distance(x, y):
    return int((x*x - y*y) ** 0.5)


print(solution(2, 4))
print(solution(1, 5))