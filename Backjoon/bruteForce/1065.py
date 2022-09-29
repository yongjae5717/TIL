def check(n):
    array = list()
    while True:
        if n >= 1:
            array.append(int(n % 10))
            n /= 10
        else:
            break

    temp = 0
    for i in range(1, len(array)):
        if i == 1:
            temp = array[i] - array[i - 1]
            continue
        elif temp != array[i] - array[i - 1]:
            return False
        temp = array[i] - array[i - 1]
    return True


# 한수: 정수의 각 자리가 등차수열을 이루는 수
# 출력: 한수의 개수

import sys

input = sys.stdin.readline

n = int(input())
result = 0
for i in range(1, n+1):
    if check(i):
        result += 1

print(result)
