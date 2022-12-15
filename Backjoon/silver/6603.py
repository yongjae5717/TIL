import sys
from itertools import permutations
input = sys.stdin.readline


def solution(lotto):
    number = lotto[1:]
    set_list = set()
    for permutation in permutations(number, 6):
        temp = list(map(int, sorted(permutation)))
        set_list.add(tuple(temp))
    result = sorted(list(set_list))
    return result


def main():
    while True:
        lotto = list(map(int, input().split()))
        if lotto[0] == 0:
            return

        result = solution(lotto)

        for i in result:
            print(*i)
        print("")


main()