def solution(food):
    answer = '0'
    food = list(enumerate(food))
    for i in reversed(food):
        index, stock = i
        for j in range((stock // 2) * 2):
            if index == 0 and stock >= 1:
                answer += str(index) * (index // 2 + 1)
            else:
                if j % 2 == 0:
                    answer += str(index)
                else:
                    answer = str(index) + answer
    return answer


print(solution([1, 3, 4, 6]))  # "1223330333221"
print(solution([1, 7, 1, 2]))  # "111303111"
