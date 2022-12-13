def solution(s):
    answer = list()
    memo = dict()

    index = 0
    for c in s:
        if c not in memo:
            answer.append(-1)
        else:
            answer.append(index - memo[c])
        memo[c] = index
        index += 1
    return answer


print(solution("banana"))
print(solution("foobar"))