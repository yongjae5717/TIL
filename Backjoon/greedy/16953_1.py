# Problem 16953
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다.
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# Input
# 첫째 줄에 A, B (1 ≤ A < B ≤ 10^9)가 주어진다.

# Output
# A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다.
# 만들 수 없는 경우에는 -1을 출력한다.
import sys


def main():
    inp, out = map(int, sys.stdin.readline().split())
    # print(inp, out)
    result = 1
    while out != inp:
        if out < inp:
            result = -1
            break
        elif out % 2 == 0:
            out = out // 2
        elif out % 10 == 1:
            out = int(str(out)[:-1])
        else:
            result = -1
            break
        result += 1
    print(result)



main()