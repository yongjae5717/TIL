import sys
from itertools import combinations, permutations
input = sys.stdin.readline


def solution():
    n = int(input())
    table = list(list(map(int, input().split())) for _ in range(n))
    population = n // 2
    total = list(i for i in range(1, n + 1))
    result = 10001
    for combination in combinations(total, population):
        total_set = set(total)
        team_a = set(combination)
        team_b = total_set - team_a

        team_a_score, team_b_score = 0, 0

        for permutation in permutations(list(team_a), 2):
            a, b = permutation
            team_a_score += table[a-1][b-1]

        for permutation in permutations(list(team_b), 2):
            a, b = permutation
            team_b_score += table[a-1][b-1]

        result = min(result, abs(team_a_score - team_b_score))

    return result


print(solution())