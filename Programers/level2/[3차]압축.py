def solution(msg):
    dictionary = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
                  "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                  "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18,
                  "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24,
                  "Y": 25, "Z": 26}

    const = 27
    jump = 0
    answer = []

    for i in range(len(msg)):
        # print(msg[i])
        if jump > 0:
            # print(jump)
            jump -= 1
            continue
        for j in range(len(msg)-i):
            if msg[i:len(msg)-j] in dictionary:
                answer.append(dictionary[msg[i:len(msg)-j]])
                dictionary[msg[i:len(msg)-j+1]] = const
                const += 1
                jump = len(msg[i:len(msg)-j]) - 1
                break
    return answer


print(solution("TOBEORNOTTOBEORTOBEORNOT"))