def solution(participant, completion):
    dictionary = dict()
    answer = list()
    for p in participant:
        if p not in dictionary:
            dictionary[p] = 1
        else:
            dictionary[p] += 1

    for c in completion:
        dictionary[c] -= 1

    for d in dictionary:
        if dictionary[d] == 1:
            answer.append(d)
    return answer[0]