def solution(arr, divisor):
    answer = list(i for i in arr if i % divisor == 0)
    answer.sort()
    if answer:
        return answer
    return [-1]