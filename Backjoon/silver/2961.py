import sys
from itertools import combinations
input = sys.stdin.readline


def main():
    n = int(input())
    food = list(list(map(int, input().split())) for _ in range(n))
    recipe = list()
    for i in range(1, n+1):
        for combination in combinations(food, i):
            recipe.append(combination)

    result = 1000000001
    for i in recipe:
        s, b = 1, 0
        for s1, b1 in i:
            s *= s1
            b += b1
        result = min(result, abs(s-b))

    return result


print(main())