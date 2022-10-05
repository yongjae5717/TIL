def solution(survey, choices):
    answer = ''

    dictionary = dict ({"R": 0, "T": 0, "F": 0, "C": 0,
                        "M": 0, "J": 0, "A": 0, "N": 0})
    points = [[3, 0], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2], [0, 3]]

    for i in range (len (survey)):
        disagree, agree = survey[i]

        disagreePoint, agreePoint = points[choices[i] - 1]
        dictionary[disagree] += disagreePoint
        dictionary[agree] += agreePoint

    answer += select ('R', 'T', dictionary)
    answer += select ('C', 'F', dictionary)
    answer += select ('J', 'M', dictionary)
    answer += select ('A', 'N', dictionary)
    return answer


def select(left, right, dictionary):
    if dictionary[left] >= dictionary[right]:
        return left
    else:
        return right