import sys
from itertools import permutations
input = sys.stdin.readline


def solution(k, array):
    result = list()
    number = list(i for i in range(10))
    for permutation in permutations(number, k + 1):
        flag = True
        for i in range(k):
            if array[i] == "<":
                if permutation[i] < permutation[i + 1]:
                    continue
                flag = False
                break
            else:
                if permutation[i] > permutation[i + 1]:
                    continue
                flag = False
                break
        if flag:
            result.append("".join(map(str, permutation)))
    return [max(result), min(result)]


def main():
    k = int(input())
    array = input().split()
    answer = solution(k, array)
    print(answer[0])
    print(answer[1])


main()