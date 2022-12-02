def solution(n):
    index = [1, 2, 4]
    answer = ""
    while n:
        if n % 3 == 0:
            answer = str(index[2]) + answer
            n = n // 3 - 1
        else:
            answer = str(index[n % 3 - 1]) + answer
            n //= 3
    return answer

print(solution(9))