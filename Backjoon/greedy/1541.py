# Problem 1541
# 세준이는 양수와 +, -, 그리고 괄호를 가지고 식을 만들었다. 그리고 나서 세준이는 괄호를 모두 지웠다.
# 그리고 나서 세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
# 괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오.

# Input
# 첫째 줄에 식이 주어진다. 식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’만으로 이루어져 있고,
# 가장 처음과 마지막 문자는 숫자이다. 그리고 연속해서 두 개 이상의 연산자가 나타나지 않고,
# 5자리보다 많이 연속되는 숫자는 없다. 수는 0으로 시작할 수 있다.
# 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# Output
# 첫째 줄에 정답을 출력한다.

import sys


def main():
    list_A = list()
    list_B = list()
    A = sys.stdin.readline().strip()
    sum = 0
    for i in range(len(A)):
        if A[i] == '-':
            list_B.append("-")
            list_A.append(sum)
            sum = 0
        elif A[i] == '+':
            list_B.append("+")
            list_A.append(sum)
            sum = 0
        elif i == len(A)-1:
            sum = sum * 10 + int(A[i])
            list_A.append(sum)
            sum = 0
        else:
            # list_A.append(A[i])
            sum = sum * 10 + int(A[i])

    result = 0
    flag = 0
    minus_sum = 0
    list_B.append("end")

    for j in range(len(list_A)):
        if j == 0:
            result = int(list_A[j])
        elif list_B[j-1] == '-':
            flag = 1
            result -= minus_sum
            minus_sum = list_A[j]
        elif list_B[j-1] == '+' and flag == 1:
            minus_sum += list_A[j]
        elif list_B[j-1] == '+' and flag == 0:
            result += list_A[j]

    result -= minus_sum
    print(result)


main()