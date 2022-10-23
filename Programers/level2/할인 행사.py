from collections import Counter


def solution(want, number, discount):
    answer = 0
    dictionary = dict()

    for i in range(len(want)):
        dictionary[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dictionary == Counter(discount[i:i+10]):
            answer += 1
    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))