# 시간 복잡도 O(n^2)
def solution(left, right):
    result = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            result += i
        else:
            result -= i
    return result


# 시간 복잡도 O(n)
# 이유: 제곱수의 약수의 개수는 홀수개
def solution2(left, right):
    result = 0
    for i in range(left, right+1):
        if int(i ** 0.5) == i ** 0.5:
            result -= i
        else:
            result += i
    return result