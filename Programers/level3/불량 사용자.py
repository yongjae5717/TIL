from itertools import permutations


def check(user, ban):
    if len(user) != len(ban):
        return False
    for i, j in zip(user, ban):
        if j == '*':
            continue
        if i != j:
            return False
    return True


def solution(user_id, banned_id):
    answer = list()
    for permutation in permutations(user_id, len(banned_id)):
        count = 0
        for user, ban in zip(permutation, banned_id):
            if check(user, ban):
                count += 1
        if count == len(banned_id) and set(permutation) not in answer:
            answer.append(set(permutation))
    return len(answer)


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))  # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))  # 3
