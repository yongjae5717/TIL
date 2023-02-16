def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            tmp = stack.pop()
            answer[tmp] = numbers[i]
        stack.append(i)
    return answer


print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
