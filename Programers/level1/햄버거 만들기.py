def solution(ingredient):
    temp = list()
    answer = 0
    for i in range(len(ingredient)):
        temp.append(ingredient[i])
        if len(temp) >= 4:
            if temp[len(temp)-4:len(temp)] == [1, 2, 3, 1]:
                del temp[len(temp)-4:len(temp)]
                answer += 1
    return answer


print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
print(solution([1, 3, 2, 1, 2, 1, 3, 1, 2]))