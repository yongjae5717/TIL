# Problem 1789
# 서로 다른 N개의 자연수의 합이 S라고 한다.
# S를 알 때, 자연수 N의 최댓값은 얼마일까?

# Input
# 첫째 줄에 자연수 S(1 ≤ S ≤ 4,294,967,295)가 주어진다.

# Output
# 첫째 줄에 자연수 N의 최댓값을 출력한다.

import sys


def main():
    S = int(sys.stdin.readline())
    sum = 0
    i = 1
    while sum < S:
        sum += i
        # print(i, sum)
        i += 1
    length = i - 1
    if sum == S:
        print(length)
    else:
        print(length-1)


main()