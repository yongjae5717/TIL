def solution(n, s):
    if n > s:
        return [-1]

    q, r = divmod(s, n)
    answer = [q] * n

    for i in range(r):
        answer[i] += 1
    return sorted(answer)


print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))