def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            a, b, c = [k for k in range(4) if k != j]
            land[i][j] += max(land[i-1][a], land[i-1][b], land[i-1][c])
    return max(land[-1])


print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))