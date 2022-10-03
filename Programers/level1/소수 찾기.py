def solution(n):
    lst = [True] * (n + 1)
    lst[0], lst[1] = False, False  # 1은 소수가 아니다

    m = int (n ** 0.5)
    for i in range (2, m + 1):
        if lst[i]:
            for j in range (2 * i, n + 1, i):
                lst[j] = False

    # print(lst)
    count = 0
    for i in range (2, n + 1):
        if lst[i]:
            count += 1
    return count


def solution2(n):
    num = set(range(2, n+1))
    for i in range(2, n+1):
        if i in num:
            num -= set(range(2*i, n+1, i))
            print(num)
    return len(num)
