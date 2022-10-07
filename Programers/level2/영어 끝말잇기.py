def solution(n, words):
    people = list ([] for _ in range (n))
    temp = ""
    for i in range (len (words)):
        people[i % n].append (words[i])

        if temp != "" and temp[len (temp) - 1] != words[i][0]:
            return [(i % n) + 1, len (people[i % n])]
        if words[i] in words[:i]:
            return [(i % n) + 1, len (people[i % n])]
        temp = words[i]

    return [0, 0]