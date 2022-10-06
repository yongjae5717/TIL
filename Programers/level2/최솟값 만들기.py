def solution(A,B):
    return sum(list(x * y for x, y in zip(sorted(A), sorted(B, reverse=True))))