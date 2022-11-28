import math


def solution(n, k):
    lst = list(i for i in range(1, n + 1))
    result = list()

    while n != 0:
        count = math.factorial(n) // n
        index, m = divmod(k - 1, count)
        result.append(lst.pop(index))

        n -= 1
        k %= count
    return result


print(solution(3, 5))